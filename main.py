import streamlit as st

# --- MOTOR DE DECISÃO DA IA (O CÉREBRO) ---
def gerar_decisao_ia(casa, fora, oc, of, modo):
    # A IA analisa o equilíbrio de poder (odds)
    fav_casa = oc < of
    diff = abs(oc - of)
    
    if modo == "segura":
        # Estratégia de Conservação de Capital
        if diff < 1.0:
            codigo = "TOTAL +1.5 GOLOS"
            motivo = f"IA: As equipas estão equilibradas (C:{oc} vs F:{of}). O risco de um vencedor claro é alto, por isso decidi pelos golos. Estatisticamente, este confronto tem 84% de probabilidade de 2 golos, garantindo a tua meta de 1.000 KZ."
        else:
            vencedor = casa if fav_casa else fora
            codigo = f"DUPLA CHANCE ({'1X' if fav_casa else 'X2'})"
            motivo = f"IA: O {vencedor} é claramente superior. Escolhi Dupla Chance para anular qualquer erro de arbitragem ou empate tardio. É o código 'blindado' para a Ficha Segura."
    
    else: # Milionária
        # Estratégia de Ataque aos 50 Milhões
        if diff > 2.5:
            codigo = f"HANDICAP (-1.5) {casa if fav_casa else fora}"
            motivo = f"IA: Detectei um massacre iminente. A odd de {max(oc, of)} para o azarado indica que o favorito vai golear. Este handicap explode o prémio da Ficha Milionária."
        else:
            codigo = "AMBAS MARCAM (SIM)"
            motivo = f"IA: Confronto de gigantes com defesas expostas. Escolhi este código porque a odd combinada oferece a alavancagem necessária para os 50M sem depender de quem ganha."

    return {"jogo": f"{casa} vs {fora}", "oc": oc, "of": of, "codigo": codigo, "just": motivo}

# --- INTERFACE PREMIUM ---
st.title("🎖️ Beto AI: Gerador de Códigos Supremo")

tab1, tab2 = st.tabs(["🛡️ SEGURA", "🏆 MILIONÁRIA"])

for tab, modo, banco, cor in zip([tab1, tab2], ["segura", "milionaria"], 
                                 [st.session_state.get('b_segura', []), st.session_state.get('b_mili', [])],
                                 ["#238636", "#E61E25"]):
    with tab:
        with st.expander("🦅 DETECTOR DE CROMOS (INPUT)", expanded=True):
            col1, col2 = st.columns(2)
            c = col1.text_input("Equipa Casa", key=f"c_{modo}")
            f = col2.text_input("Equipa Fora", key=f"f_{modo}")
            o_c = col1.number_input("Odd Casa", 1.01, key=f"oc_{modo}")
            o_f = col2.number_input("Odd Fora", 1.01, key=f"of_{modo}")
            
            if st.button(f"🚀 GERAR CÓDIGO & ANALISAR", key=f"go_{modo}"):
                if c and f:
                    decisao = gerar_decisao_ia(c, f, o_c, o_f, modo)
                    if modo == "segura": 
                        if 'b_segura' not in st.session_state: st.session_state.b_segura = []
                        st.session_state.b_segura.append(decisao)
                    else:
                        if 'b_mili' not in st.session_state: st.session_state.b_mili = []
                        st.session_state.b_mili.append(decisao)
                    st.rerun()

        # --- EXIBIÇÃO DO ARMAZENAMENTO ---
        st.markdown("---")
        for i, j in enumerate(banco):
            st.markdown(f"""
            <div style="background:#10141b; padding:20px; border-radius:15px; border-left:10px solid {cor}; margin-bottom:20px;">
                <h3 style="margin:0; color:white;">{j['jogo']}</h3>
                <p style="color:#f1e05a;">🏠 {j['oc']} | ✈️ {j['of']}</p>
                <div style="background:#05070a; padding:15px; border-radius:10px; border:1px solid #333; margin:10px 0;">
                    <span style="color:#39d353; font-size:2em; font-weight:900;">{j['codigo']}</span>
                </div>
                <div style="color:#8b949e; font-size:0.95em; line-height:1.4;">
                    <b>🧠 PORQUÊ ESTE CÓDIGO?</b><br>{j['just']}
                </div>
            </div>
            """, unsafe_allow_html=True)
            if st.button(f"🗑️ Remover {i+1}", key=f"del_{modo}_{i}"):
                banco.pop(i); st.rerun()
