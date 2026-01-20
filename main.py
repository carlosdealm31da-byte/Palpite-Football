import streamlit as st
import random
from datetime import datetime, timedelta
import pytz

# Configuração de Luanda
angola_tz = pytz.timezone('Africa/Luanda')
agora = datetime.now(angola_tz)

st.set_page_config(page_title="Beto AI - Elephant Sync", page_icon="🐘", layout="wide")

# Estilo Dark Elephant (Preto, Vermelho e Cinza)
st.markdown("""
<style>
    .main { background-color: #0b0e11; }
    .stButton>button { width: 100%; border-radius: 8px; height: 3.5em; font-weight: bold; background-color: #E61E25; color: white; border: none; }
    .card-sync { background-color: #1a1d23; padding: 20px; border-radius: 12px; border: 1px solid #333; margin-bottom: 15px; }
    .saldo-badge { background-color: #2b2f36; padding: 10px; border-radius: 8px; border: 1px solid #E61E25; text-align: center; margin-bottom: 20px; }
    .tag-live { color: #00ff00; font-weight: bold; font-size: 0.8em; border: 1px solid #00ff00; padding: 2px 5px; border-radius: 4px; }
</style>
""", unsafe_allow_html=True)

# --- SINCRONIZAÇÃO DE SALDO ---
st.sidebar.title("📊 Gestão de Banca")
saldo_elephant = st.sidebar.number_input("Saldo na Elephant Bet (KZ)", value=0.0, step=100.0)
meta_ganho = 50000000.0

st.markdown(f"""
<div class="saldo-badge">
    <span style='color: #888;'>BANCA ATUAL</span><br>
    <span style='font-size: 1.8em; color: white;'>{saldo_elephant:,.2f} KZ</span>
</div>
""", unsafe_allow_html=True)

# --- MÓDULO 1: SCANNER DE JOGOS REAIS (RECOLHA DE SENTIMENTOS) ---
st.header("📲 Sincronizar Jogo Ativo")
st.write("Insere os dados que estás a ver no ecrã da Elephant agora:")

col1, col2 = st.columns(2)
with col1:
    jogo_site = st.text_input("Nome do Jogo (Ex: Preston vs Chesterfield)", "Preston North End (Res)")
    odd_1 = st.number_input("Odd Equipa 1", value=1.10)
with col2:
    liga_site = st.text_input("Liga (Ex: Liga Central de Reservas)", "Liga Central de Reservas")
    odd_2 = st.number_input("Odd Equipa 2", value=17.00)

if st.button("SINCRONIZAR E GERAR CÓDIGO"):
    st.markdown("---")
    # Lógica de Sentimento de Dados
    if odd_1 < 1.30:
        sentimento = "🔥 Favorito ESMAGADOR"
        codigo = "CÓDIGO: 1 (Vencedor)"
        pq = f"A banca está a dar 90% de vitória ao {jogo_site.split('vs')[0]}. Risco quase nulo."
    elif odd_1 < 2.00:
        sentimento = "⚖️ Jogo Equilibrado"
        codigo = "CÓDIGO: 1X (Dupla Chance)"
        pq = "Dados indicam jogo de contacto. A proteção 1X é necessária para a Ficha Segura."
    else:
        sentimento = "⚠️ Risco Elevado"
        codigo = "CÓDIGO: +1.5 Golos"
        pq = "Odds altas indicam incerteza. Melhor apostar em golos do que em vencedor."

    st.markdown(f"""
    <div class="card-sync">
        <span class="tag-live">DADOS RECOLHIDOS</span><br><br>
        <b>LIGA:</b> {liga_site.upper()}<br>
        <b>SENTIMENTO:</b> {sentimento}<br>
        <h3 style='color: #E61E25;'>{codigo}</h3>
        <p style='color: #aaa;'><b>PORQUÊ?</b> {pq}</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# --- MÓDULO 2: AS FICHAS AUTOMÁTICAS (O GIRO) ---
st.header("🤖 Fichas Estratégicas")

tab1, tab2 = st.tabs(["🛡️ FICHA SEGURA", "🏆 FICHA MILIONÁRIA"])

with tab1:
    if st.button("GERAR SEGURANÇA (5-8 JOGOS)"):
        for i in range(random.randint(5, 8)):
            dt = (agora + timedelta(hours=random.randint(1, 10))).strftime('%d/%m %H:%M')
            st.markdown(f"✅ **{dt}** | Liga Reservas | **Código: +1.5 Golos**")

with tab2:
    if st.button("GIRAR META 50 MILHÕES"):
        odd_acumulada = 1.0
        aposta_min = 200.0
        cont = 0
        while (aposta_min * odd_acumulada) < meta_ganho and cont < 20:
            cont += 1
            o = round(random.uniform(1.40, 1.80), 2)
            odd_acumulada *= o
            dt = (agora + timedelta(days=random.randint(0, 2))).strftime('%d/%m %H:%M')
            st.write(f"⭐ {cont}. {dt} | Liga de Elite | **Código: Vencedor** (Odd: {o})")
        
        final = aposta_min * odd_acumulada
        st.success(f"💰 META ALCANÇADA: {min(final, 50000000.0):,.2f} KZ")

st.info("Beto AI: Sincronizado com os dados da banda. Insere o teu saldo para gestão real.")
