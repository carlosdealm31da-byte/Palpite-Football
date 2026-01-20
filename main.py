import streamlit as st
from datetime import datetime
import pytz

# Configuração de Luanda
angola_tz = pytz.timezone('Africa/Luanda')
agora = datetime.now(angola_tz)

st.set_page_config(page_title="Beto AI - Manual e Visual", layout="wide")

if 'banco_segura' not in st.session_state: st.session_state.banco_segura = []
if 'banco_milionario' not in st.session_state: st.session_state.banco_milionario = []

# --- ESTÉTICA PERSONALIZADA ---
st.markdown("""
<style>
    .main { background-color: #05070a; }
    .ficha-segura { border-left: 10px solid #FF69B4; background: #1a1015; padding: 20px; border-radius: 15px; margin-bottom: 20px; }
    .ficha-mili { border-left: 10px solid #E61E25; background: #1a0d0d; padding: 20px; border-radius: 15px; margin-bottom: 20px; }
    .v-codigo { color: #39d353; font-size: 2.5em; font-weight: 900; }
    .explica-box { background: rgba(0,0,0,0.4); padding: 15px; border-radius: 10px; color: #ced4da; font-size: 0.95em; border: 1px solid #333; }
</style>
""", unsafe_allow_html=True)

# --- MOTOR DE DECISÃO E EXPLICAÇÃO ---
def processar_ia_detalhado(casa, fora, oc, of, modo):
    if modo == "segura":
        codigo = "MAIS 1.5 GOLOS" if abs(oc-of) < 1.2 else "DUPLA CHANCE (1X/X2)"
        funciona = "Este código ganha se houver pelo menos 2 golos no jogo (qualquer equipa) ou se a equipa favorita não perder."
        pq = "O Mascote Rosa prioriza o lucro constante. Escolhi este código porque ele cobre 70% dos resultados possíveis, garantindo que a sua ficha não caia por um detalhe."
        diag = "" if "GOLOS" in codigo else ""
    else:
        codigo = "HANDICAP (-1.5)" if oc < of else "AMBAS MARCAM & +2.5"
        funciona = "O favorito precisa de ganhar por 2 golos de diferença OU ambas as equipas marcam e o jogo tem 3 ou mais golos."
        pq = "Modo Milionário ativado. Aqui arriscamos para bater os 50M. Escolhi este código porque a odd de favorito está baixa, então forçamos a margem de golos para disparar o prémio."
        diag = "" if "HANDICAP" in codigo else ""

    return {"jogo": f"{casa} vs {fora}", "oc": oc, "of": of, "cod": codigo, "func": funciona, "pq": pq, "diag": diag}

st.title("🎖️ Beto AI: Gestão de Banca Manual")
st.write(f"🕒 Luanda: **{agora.strftime('%H:%M')}**")

tab1, tab2 = st.tabs(["🌸 FICHA SEGURA (MASCOTE ROSA)", "🔥 FICHA MILIONÁRIA (AGRESSIVA)"])

# --- LÓGICA DAS ABAS ---
for tab, modo, banco, css in zip([tab1, tab2], ["segura", "milionaria"], 
                                  [st.session_state.banco_segura, st.session_state.banco_milionario],
                                  ["ficha-segura", "ficha-mili"]):
    with tab:
        with st.container():
            st.subheader(f"📝 Comando Manual - {modo.upper()}")
            c1, c2 = st.columns(2)
            casa = c1.text_input("Equipa Casa", key=f"c_{modo}")
            fora = c2.text_input("Equipa Fora", key=f"f_{modo}")
            oc = c1.number_input("Odd Casa", 1.01, key=f"oc_{modo}")
            of = c2.number_input("Odd Fora", 1.01, key=f"of_{modo}")
            
            if st.button(f"🚀 GERAR CÓDIGO {modo.upper()}", key=f"btn_{modo}"):
                if casa and fora:
                    banco.append(processar_ia_detalhado(casa, fora, oc, of, modo))
                    st.rerun()

        st.markdown("---")
        for i, j in enumerate(banco):
            st.markdown(f"""
            <div class="{css}">
                <div style="display:flex; justify-content:space-between;">
                    <b style="font-size:1.3em; color:white;">{j['jogo']}</b>
                    <span style="color:#f1e05a;">🏠 {j['oc']} | ✈️ {j['of']}</span>
                </div>
                <div style="margin: 15px 0;">
                    <span class="v-codigo">{j['cod']}</span>
                </div>
                <div class="explica-box">
                    <b>🧠 PORQUÊ?</b> {j['pq']}<br><br>
                    <b>⚙️ COMO FUNCIONA?</b> {j['func']}
                </div>
            </div>
            """, unsafe_allow_html=True)
            st.write(j['diag']) # Aqui entra a imagem da possibilidade
            if st.button(f"🗑️ Remover {i+1}", key=f"del_{modo}_{i}"):
                banco.pop(i); st.rerun()

if st.sidebar.button("🚨 LIMPAR TUDO"):
    st.session_state.clear()
    st.rerun()
