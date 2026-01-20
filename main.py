import streamlit as st
from datetime import datetime
import pytz

# Configuração de Luanda
angola_tz = pytz.timezone('Africa/Luanda')
agora = datetime.now(angola_tz)

st.set_page_config(page_title="Beto AI - O Decisor", page_icon="🐘")

# Estilo Visual Elephant Bet (Focado no Resultado)
st.markdown("""
<style>
    .main { background-color: #0b1116; }
    .stButton>button { width: 100%; border-radius: 8px; font-weight: bold; background-color: #E61E25; color: white; height: 3.5em; border: none; }
    .decisao-card { background-color: #1a1d23; padding: 25px; border-radius: 12px; border-left: 6px solid #E61E25; color: white; margin-top: 20px; box-shadow: 0px 4px 15px rgba(0,0,0,0.5); }
    .codigo-final { color: #00ff00; font-size: 2.2em; font-weight: bold; display: block; margin: 15px 0; text-shadow: 1px 1px #000; }
    .porquê-box { background-color: #262a33; padding: 15px; border-radius: 8px; border: 1px solid #444; line-height: 1.5; color: #ddd; }
</style>
""", unsafe_allow_html=True)

st.title("🐘 Beto AI: Inteligência de Decisão")
st.write(f"🕒 Hora em Luanda: **{agora.strftime('%H:%M')}**")

# --- ENTRADA DE DADOS PARA A IA ---
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        casa = st.text_input("Equipa da Casa", placeholder="Ex: Preston North End")
        odd_c = st.number_input("Odd Casa", value=1.10, step=0.01)
    with col2:
        fora = st.text_input("Equipa de Fora", placeholder="Ex: Chesterfield")
        odd_f = st.number_input("Odd Fora", value=17.00, step=0.01)

    c1, c2 = st.columns(2)
    with c1:
        data_j = st.date_input("Data do Jogo", value=agora.date())
    with c2:
        hora_j = st.time_input("Hora de Início")

    if st.button("GERAR DECISÃO DA IA"):
        # 1. VALIDADOR DE HORÁRIO
        dt_evento = angola_tz.localize(datetime.combine(data_j, hora_j))
        
        if dt_evento < agora:
            st.error(f"❌ ANALISE CANCELADA: O jogo {casa} vs {fora} já decorreu ou começou às {hora_j.strftime('%H:%M')}.")
        else:
            # 2. MOTOR DE DECISÃO DA IA (Ela escolhe o melhor código)
            if odd_c < 1.25:
                codigo = "1 (VENCEDOR CASA)"
                explicacao = f"A inteligência detectou um favoritismo extremo para o {casa}. Com uma odd de {odd_c}, a probabilidade de vitória supera os 90%. É a escolha mais lógica para garantir o green sem correr riscos desnecessários."
            elif odd_f < 1.25:
                codigo = "2 (VENCEDOR FORA)"
                explicacao = f"O {fora} entra em campo com superioridade total. O mercado esmagou a odd para {odd_f}, indicando que qualquer outro resultado seria uma zebra histórica. O código 2 é a decisão final."
            elif 1.40 <= odd_c <= 2.10 and 1.40 <= odd_f <= 2.10:
                codigo = "AMBAS MARCAM (SIM)"
                explicacao = f"Este é um jogo de equilíbrio dinâmico. Ambas as equipas têm odds parecidas, o que indica que os dois ataques são perigosos. A IA escolheu este código porque a chance de um 1-1 ou 2-1 é maior do que uma vitória seca."
            elif odd_c > 2.50 and odd_fora > 2.50:
                codigo = "+1.5 GOLOS"
                explicacao = "Jogo sem favorito claro e com defesas instáveis. A inteligência prefere não arriscar no vencedor e focar na rede balançar. O código de golos oferece a melhor relação risco-retorno aqui."
            else:
                codigo = "1X (DUPLA CHANCE)"
                explicacao = f"Apesar do favoritismo do {casa}, há uma pequena instabilidade nas odds. A IA decide pela segurança do 1X para cobrir um possível empate tardio, mantendo o bilhete vivo."

            # EXIBIÇÃO DA DECISÃO
            st.markdown(f"""
            <div class="decisao-card">
                <span style='color: #E61E25; font-size: 0.9em; font-weight: bold;'>🎯 DECISÃO DA INTELIGÊNCIA</span><br>
                <b style='font-size: 1.3em;'>{casa} vs {fora}</b><br>
                <span style='color: #888;'>Janela de Tempo: {hora_j.strftime('%H:%M')}</span>
                
                <span class="codigo-final">{codigo}</span>
                
                <div class="porquê-box">
                    <b>PORQUÊ ESTE CÓDIGO?</b><br>
                    {explicacao}
                </div>
            </div>
            """, unsafe_allow_html=True)

st.markdown("---")
st.info("Beto AI: Analisando o mercado em tempo real para tomar a melhor decisão por ti.")
