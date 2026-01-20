import streamlit as st
import random
from datetime import datetime, time
import pytz

# Configuração de Luanda
angola_tz = pytz.timezone('Africa/Luanda')
agora = datetime.now(angola_tz)

st.set_page_config(page_title="Beto AI - Memória de Guerra", layout="wide")

# Inicializar Bancos de Armazenamento Automático
if 'banco_segura' not in st.session_state: st.session_state.banco_segura = []
if 'banco_milionario' not in st.session_state: st.session_state.banco_milionario = []

st.markdown("""
<style>
    .main { background-color: #0b0e11; }
    .quadrado-x { 
        background-color: #1a1d23; padding: 25px; border-radius: 15px; 
        border: 2px solid #333; margin-bottom: 20px; border-left: 10px solid #238636;
    }
    .v-codigo { color: #39d353; font-size: 2.3em; font-weight: bold; }
    .memoria-box { background: #0d1117; padding: 15px; border-radius: 10px; border: 1px solid #444; margin-top: 15px; }
</style>
""", unsafe_allow_html=True)

st.title("🎖️ Beto AI: Armazenamento e Inteligência")
st.write(f"🕒 Central de Luanda: **{agora.strftime('%H:%M')}**")

# --- FUNÇÃO DE ANÁLISE E CRÍTICA ---
def analisar_e_armazenar(casa, fora, o1, hora, modo):
    # Regra de Bloqueio por Horário
    h, m = map(int, hora.split(':'))
    horario_j = angola_tz.localize(datetime.combine(agora.date(), time(h, m)))
    if horario_j <= agora: return None

    # Sugestão e Opinião da IA
    if modo == "segura":
        codigo = "TOTAL +1.5 GOLOS" if o1 < 1.4 else "DUPLA CHANCE"
        opiniao = f"IA: Jogo apto para Ficha Segura. Foco em atingir > 1.000 KZ com baixo risco."
        odd_f = 1.35
    else:
        codigo = "HANDICAP (-1.5)" if o1 < 1.8 else "AMBAS MARCAM"
        opiniao = f"IA: Escolha valente para a Milionária. Contribui para a meta de 50M."
        odd_f = o1 * 1.8

    return {"jogo": f"{casa} vs {fora}", "codigo": codigo, "obs": opiniao, "hora": hora, "odd": odd_f}

# --- ABAS ---
tab1, tab2 = st.tabs(["🛡️ FICHA SEGURA (Regra 5-8)", "🏆 FICHA MILIONÁRIA (Inteirar até 40)"])

for tab, modo, banco, cor in zip([tab1, tab2], ["segura", "milionaria"], 
                                 [st.session_state.banco_segura, st.session_state.banco_milionario],
                                 ["#238636", "#E61E25"]):
    with tab:
        # CABEÇALHO DE ARMAZENAMENTO
        odd_t = 1.0
        for item in banco: odd_t *= item['odd']
        st.markdown(f"### 📦 Armazenamento: **{200*odd_t:,.2f} KZ** | Jogos: **{len(banco)}**")

        # MODO MANUAL INTEGRADO (O General manda, a IA analisa)
        with st.expander("➕ INTEIRAR JOGO MANUALMENTE", expanded=False):
            c1, c2, c3 = st.columns(3)
            mcasa = c1.text_input("Casa", key=f"mc_{modo}")
            mfora = c2.text_input("Fora", key=f"mf_{modo}")
            mhora = c3.text_input("Hora (HH:MM)", "20:00", key=f"mh_{modo}")
            modd = st.number_input("Odd", 1.01, key=f"mo_{modo}")
            
            if st.button("🛡️ ANALISAR E GUARDAR NO BANCO", key=f"save_{modo}"):
                res = analisar_e_armazenar(mcasa, mfora, modd, mhora, modo)
                if res:
                    banco.append(res)
                    st.success("Jogo analisado e movido para o armazenamento!")
                    st.rerun()

        # VISUALIZAÇÃO DO BANCO
        st.markdown("---")
        for i, jogo in enumerate(banco):
            st.markdown(f"""
            <div class="quadrado-x" style="border-left-color: {cor}">
                <small>🕒 {jogo['hora']} | MEMÓRIA {i+1}</small>
                <div style="font-size:1.5em; font-weight:bold; color:white;">{jogo['jogo']}</div>
                <span class="v-codigo">{jogo['codigo']}</span>
                <div class="memoria-box"><b>💡 OPINIÃO DO BETO AI:</b><br>{jogo['obs']}</div>
            </div>
            """, unsafe_allow_html=True)
            if st.button(f"🗑️ Remover Jogo {i+1}", key=f"rem_{modo}_{i}"):
                banco.pop(i); st.rerun()

if st.sidebar.button("🗑️ LIMPAR TODOS OS ARMAZENAMENTOS"):
    st.session_state.clear()
    st.rerun()
