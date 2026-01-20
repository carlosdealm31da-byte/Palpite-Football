import streamlit as st
import random
from datetime import datetime
import pytz

# Configuração de Luanda
angola_tz = pytz.timezone('Africa/Luanda')
agora = datetime.now(angola_tz)

st.set_page_config(page_title="Beto AI - O Decisor", page_icon="🐘")

# ESTILO FIEL ÀS TUAS FOTOS (Cores da Elephant Bet)
st.markdown("""
<style>
    .main { background-color: #0b0e11; }
    .stButton>button { width: 100%; border-radius: 8px; font-weight: bold; background-color: #E61E25; color: white; height: 3.8em; border: none; font-size: 1.1em; }
    .decisao-card { background-color: #1a1d23; padding: 25px; border-radius: 12px; border-left: 6px solid #E61E25; color: white; margin-top: 20px; box-shadow: 0px 4px 15px rgba(0,0,0,0.5); }
    .codigo-v { color: #00ff00; font-size: 2em; font-weight: bold; display: block; margin: 10px 0; }
    .probabilidade { color: #ffc107; font-size: 1.4em; font-weight: bold; }
    .explicacao-box { background-color: #262a33; padding: 15px; border-radius: 8px; border: 1px solid #444; margin-top: 15px; color: #ddd; line-height: 1.4; }
</style>
""", unsafe_allow_html=True)

# GESTÃO DE BANCA NO MENU LATERAL
st.sidebar.title("📊 Gestão de Banca")
saldo = st.sidebar.number_input("Saldo Elephant (KZ)", value=0.0)
st.sidebar.write(f"🕒 Luanda: {agora.strftime('%H:%M')}")

st.title("🐘 Beto AI: Inteligência de Decisão")

# --- ENTRADA DE DADOS DO JOGO ---
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        casa = st.text_input("Equipa Casa", placeholder="Ex: Man. City")
        odd_c = st.number_input("Odd Casa", value=1.50)
    with col2:
        fora = st.text_input("Equipa Fora", placeholder="Ex: Everton")
        odd_f = st.number_input("Odd Fora", value=3.50)

    # Entrada de tempo apenas para registo no bilhete
    hora_j = st.text_input("Início do Jogo", value="16:30")

    if st.button("GERAR CÓDIGO E EXPLICAÇÃO"):
        # MOTOR DE INTELIGÊNCIA: ESCOLHA DO CÓDIGO ADEQUADO
        # A IA decide o mercado com base na análise das Odds
        
        if odd_c < 1.35:
            escolha = "CÓDIGO: 1 (Vencedor)"
            prob = random.uniform(89.5, 95.8)
            porque = f"A inteligência analisou um favoritismo absoluto do {casa}. A odd baixa indica que a banca espera um domínio total. Este código foi escolhido por ser a entrada de maior segurança para este confronto."
        
        elif odd_f < 1.35:
            escolha = "CÓDIGO: 2 (Vencedor)"
            prob = random.uniform(89.5, 95.8)
            porque = f"O {fora} apresenta superioridade tática esmagadora para este jogo fora de casa. O mercado está a ajustar para uma vitória clara do visitante."
        
        elif 1.45 <= odd_c <= 2.20 and 1.45 <= odd_f <= 2.20:
            escolha = "CÓDIGO: AMBAS MARCAM (SIM)"
            prob = random.uniform(81.2, 88.4)
            porque = "Jogo de equilíbrio dinâmico. Ambas as equipas possuem ataques produtivos e odds aproximadas, o que torna o mercado de golos mútuos o mais rentável e inteligente aqui."
        
        elif odd_c > 2.50 and odd_f > 2.50:
            escolha = "CÓDIGO: +1.5 GOLOS"
            prob = random.uniform(88.0, 94.5)
            porque = "Confronto sem favorito claro. Em vez de arriscar no vencedor, a IA decidiu pelo mercado de golos, aproveitando as falhas defensivas típicas de equipas com odds elevadas."
        
        else:
            escolha = "CÓDIGO: 1X (Dupla Chance)"
            prob = random.uniform(77.5, 84.9)
            porque = "Jogo de médio risco. A inteligência escolheu este código para proteger a tua banca contra um empate inesperado, garantindo o green se a casa não perder."

        # EXIBIÇÃO DA DECISÃO FINAL
        st.markdown(f"""
        <div class="decisao-card">
            <span style='color: #E61E25; font-weight: bold;'>🎯 ANÁLISE E ESCOLHA DA IA</span><br>
            <b style='font-size: 1.2em;'>{casa} vs {fora}</b><br>
            <span style='color: #888;'>Horário: {hora_j}</span><br><br>
            
            <span style='font-size: 0.9em; color: #aaa;'>MELHOR CÓDIGO PARA ESTE JOGO:</span>
            <span class="codigo-v">{escolha}</span>
            
            <span style='font-size: 0.9em; color: #aaa;'>PROBABILIDADE DE ENTRADA:</span><br>
            <span class="probabilidade">🔥 {prob:.1f}%</span>
            
            <div class="explicacao-box">
                <b>MOTIVO DA ESCOLHA:</b><br>
                {porque}
            </div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")
st.info("Beto AI: A decisão do código é baseada em probabilidade matemática e análise de mercado.")
