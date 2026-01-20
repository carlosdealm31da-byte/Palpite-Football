import streamlit as st
from datetime import datetime
import pytz

# Configuração de Luanda
angola_tz = pytz.timezone('Africa/Luanda')
agora = datetime.now(angola_tz)

st.set_page_config(page_title="Beto AI - Comando Manual", layout="wide")

# Inicializar Armazenamento
if 'banco_segura' not in st.session_state: st.session_state.banco_segura = []
if 'banco_milionario' not in st.session_state: st.session_state.banco_milionario = []

st.markdown("""
<style>
    .main { background-color: #05070a; }
    .card-jogo { 
        background: #10141b; padding: 25px; border-radius: 15px; 
        border: 1px solid #333; margin-bottom: 20px;
    }
    .v-codigo { color: #39d353; font-size: 2.5em; font-weight: 900; line-height: 1; }
    .motivo-box { 
        background: rgba(255, 255, 255, 0.05); padding: 15px; 
        border-radius: 10px; border-left: 5px solid #f1e05a; color: #8b949e; 
    }
    .stButton>button { width: 100%; border-radius: 10px; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

# --- MOTOR DE DECISÃO (A IA SÓ GERA O CÓDIGO) ---
def processar_ia(casa, fora, oc, of, modo):
    diff = abs(oc - of)
    if modo == "segura":
        if diff < 1.0:
            cod, pq = "TOTAL +1.5 GOLOS", "Equilíbrio total nas odds. O mercado de golos é o único porto seguro para evitar perdas no 1x2."
        else:
            cod, pq = "DUPLA CHANCE", "Favoritismo claro detectado. Usamos a cobertura dupla para garantir a meta de 1.000 KZ sem sustos."
    else:
        if diff > 2.0:
            cod, pq = "HANDICAP (-1.5)", "Diferença técnica abismal. Para chegar aos 50M, este é o multiplicador ideal para o favorito."
        else:
            cod, pq = "AMBAS MARCAM", "Confronto direto de alta voltagem. A odd sugere que ninguém fica a zeros. Alavancagem máxima."
    
    return {"jogo": f"{casa} vs {fora}", "oc": oc, "of": of, "codigo": cod, "just": pq}

st.title("🎖️ Beto AI: Comando Manual de Elite")
st.write(f"🕒 Operação Luanda: **{agora.strftime('%H:%M')}**")

# --- ABAS DE OPERAÇÃO ---
tab1, tab2 = st.tabs(["🛡️ FICHA SEGURA", "🏆 FICHA MILIONÁRIA"])

for tab, modo, banco, cor in zip([tab1, tab2], ["segura", "milionaria"], 
                                 [st.session_state.banco_segura, st.session_state.banco_milionario],
                                 ["#238636", "#E61E25"]):
    with tab:
        # INPUT MANUAL OBRIGATÓRIO
        st.subheader("📝 Inserir Dados do Confronto")
        with st.container():
            c1, c2 = st.columns(2)
            equipa_c = c1.text_input("Equipa Casa", key=f"c_{modo}", placeholder="Ex: Qarabag")
            equipa_f = c2.text_input("Equipa Fora", key=f"f_{modo}", placeholder="Ex: Frankfurt")
            
            c3, c4 = st.columns(2)
            odd_c = c3.number_input("Odd Casa", 1.01, format="%.2f", key=f"oc_{modo}")
            odd_f = c4.number_input("Odd Fora", 1.01, format="%.2f", key=f"of_{modo}")
            
            if st.button(f"🚀 GERAR CÓDIGO {modo.upper()}", key=f"btn_{modo}"):
                if equipa_c and equipa_f:
                    resultado = processar_ia(equipa_c, equipa_f, odd_c, odd_f, modo)
                    banco.append(resultado)
                    st.rerun()

        # LISTAGEM DE RESULTADOS
        st.markdown("---")
        for i, j in enumerate(banco):
            st.markdown(f"""
            <div class="card-jogo" style="border-top: 5px solid {cor}">
                <div style="display: flex; justify-content: space-between;">
                    <span style="color: white; font-weight: bold; font-size: 1.2em;">{j['jogo']}</span>
                    <span style="color: #f1e05a;">🏠 {j['oc']} | ✈️ {j['of']}</span>
                </div>
                <div style="margin: 20px 0;">
                    <small style="color: #8b949e;">CÓDIGO GERADO PELA IA:</small><br>
                    <span class="v-codigo">{j['codigo']}</span>
                </div>
                <div class="motivo-box">
                    <b>🧠 PORQUÊ ESTA ESCOLHA?</b><br>
                    {j['just']}
                </div>
            </div>
            """, unsafe_allow_html=True)
            if st.button(f"🗑️ Remover Jogo {i+1}", key=f"del_{modo}_{i}"):
                banco.pop(i); st.rerun()

if st.sidebar.button("🚨 LIMPAR TODO O SISTEMA"):
    st.session_state.clear()
    st.rerun()
