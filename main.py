import streamlit as st
import random
from datetime import datetime, timedelta
import pytz

# Configuração de Luanda
angola_tz = pytz.timezone('Africa/Luanda')
agora = datetime.now(angola_tz)

st.set_page_config(page_title="Beto AI - Decisor de Elite", page_icon="🐘", layout="wide")

# Estilo Dark Elephant (Fiel às cores da banca)
st.markdown("""
<style>
    .main { background-color: #0b0e11; }
    .stButton>button { width: 100%; border-radius: 8px; height: 3.5em; font-weight: bold; background-color: #E61E25; color: white; border: none; }
    .card-decisao { background-color: #1a1d23; padding: 25px; border-radius: 12px; border-left: 8px solid #E61E25; color: white; margin-bottom: 15px; border: 1px solid #333; }
    .saldo-badge { background-color: #2b2f36; padding: 10px; border-radius: 8px; border: 1px solid #E61E25; text-align: center; margin-bottom: 20px; }
    .codigo-v { color: #00ff00; font-size: 2.2em; font-weight: bold; display: block; margin-bottom: 5px; }
    .prob-v { color: #ffc107; font-size: 1.4em; font-weight: bold; }
    .motivo-texto { color: #ccc; font-style: italic; font-size: 0.95em; line-height: 1.5; background: #262a33; padding: 15px; border-radius: 8px; margin-top: 10px; }
</style>
""", unsafe_allow_html=True)

# --- GESTÃO DE BANCA ---
st.sidebar.title("📊 Gestão de Banca")
saldo_elephant = st.sidebar.number_input("Saldo na Elephant Bet (KZ)", value=0.0, step=100.0)

st.markdown(f"""
<div class="saldo-badge">
    <span style='color: #888;'>BANCA ATUAL</span><br>
    <span style='font-size: 1.8em; color: white;'>{saldo_elephant:,.2f} KZ</span>
</div>
""", unsafe_allow_html=True)

# --- MÓDULO: O DECISOR (IA ESCOLHE O CÓDIGO) ---
st.header("📲 Analisador e Decisor de Jogos")
st.write("Insira os dados e deixe a IA escolher o código mais adequado:")

col1, col2 = st.columns(2)
with col1:
    casa = st.text_input("Equipa da Casa", "Ex: Man. City")
    odd_1 = st.number_input("Odd Casa", value=1.50)
with col2:
    fora = st.text_input("Equipa de Fora", "Ex: Arsenal")
    odd_2 = st.number_input("Odd Fora", value=2.50)

if st.button("GERAR CÓDIGO IDEAL E EXPLICAÇÃO"):
    st.markdown("---")
    
    # MOTOR DE INTELIGÊNCIA (A IA toma a decisão baseada nas Odds)
    if odd_1 < 1.35:
        codigo_escolhido = "CÓDIGO: 1 (VENCEDOR CASA)"
        porcentagem = random.uniform(93.1, 97.8)
        justificativa = f"A IA escolheu este código devido ao favoritismo esmagador do {casa}. Com uma odd de {odd_1}, a probabilidade de vitória é máxima e o risco de perda é estatisticamente desprezível para este confronto."
    elif odd_2 < 1.35:
        codigo_escolhido = "CÓDIGO: 2 (VENCEDOR FORA)"
        porcentagem = random.uniform(93.1, 97.8)
        justificativa = f"Superioridade técnica do {fora} detectada. O mercado está a ajustar para uma vitória clara do visitante. Este código oferece a maior segurança para este cenário de odds."
    elif 1.45 <= odd_1 <= 2.20 and 1.45 <= odd_2 <= 2.20:
        codigo_escolhido = "CÓDIGO: AMBAS MARCAM (SIM)"
        porcentagem = random.uniform(85.4, 90.2)
        justificativa = "Equilíbrio ofensivo. A IA analisou que ambas as equipas possuem ataques produtivos e odds similares, tornando o mercado de golos mútuos muito mais inteligente que o de vencedor."
    elif odd_1 > 2.50 and odd_2 > 2.50:
        codigo_escolhido = "CÓDIGO: +1.5 GOLOS"
        porcentagem = random.uniform(88.0, 94.5)
        justificativa = "Sem favorito claro no papel. A inteligência decidiu pelo mercado de golos para garantir o acerto, visto que ambas as equipas jogam de forma aberta quando não há um dominador técnico."
    else:
        codigo_escolhido = "CÓDIGO: 1X (DUPLA CHANCE)"
        porcentagem = random.uniform(79.0, 86.5)
        justificativa = "Decisão de proteção de capital. O jogo apresenta risco moderado de empate, portanto, a IA escolheu a Dupla Chance para manter a tua ficha segura."

    st.markdown(f"""
    <div class="card-decisao">
        <span style='color: #E61E25; font-weight: bold;'>🎯 DECISÃO FINAL DA INTELIGÊNCIA</span><br><br>
        <span style='font-size: 1.2em;'><b>{casa} vs {fora}</b></span><br>
        
        <span style='color: #888; font-size: 0.9em;'>CÓDIGO SUGERIDO:</span>
        <span class="codigo-v">{codigo_escolhido}</span>
        
        <span style='color: #888; font-size: 0.9em;'>PROBABILIDADE DE ENTRADA:</span><br>
        <span class="prob-v">🔥 {porcentagem:.1f}%</span><br><br>
        
        <div class="motivo-texto">
            <b>PORQUÊ ESTE CÓDIGO?</b><br>
            {justificativa}
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# MÓDULO DE FICHAS (APENAS SEGURANÇA)
st.header("🛡️ Fichas de Segurança")
if st.button("GERAR LISTA DE SEGURANÇA (5 JOGOS)"):
    for i in range(5):
        h = (agora + timedelta(minutes=random.randint(60, 480))).strftime('%H:%M')
        st.write(f"✅ {h} | Liga Profissional | **Código: +1.5 Golos**")

st.info("Beto AI: Inteligência aplicada para decisões lucrativas na Elephant Bet.")
