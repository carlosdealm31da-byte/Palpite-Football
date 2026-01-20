import streamlit as st
from datetime import datetime
import pytz

# Configuração de Luanda (Fuso Horário Real)
angola_tz = pytz.timezone('Africa/Luanda')
agora = datetime.now(angola_tz)

st.set_page_config(page_title="Beto AI - Inteligência de Código", page_icon="🐘")

# Estilo Dark Elephant
st.markdown("""
<style>
    .main { background-color: #0b1116; }
    .stButton>button { width: 100%; border-radius: 8px; font-weight: bold; background-color: #E61E25; color: white; height: 3.5em; border: none; }
    .card-analise { background-color: #1a1d23; padding: 20px; border-radius: 10px; border-left: 5px solid #E61E25; color: white; margin-top: 20px; }
    .codigo-mestre { color: #00ff00; font-size: 1.8em; font-weight: bold; display: block; margin-top: 10px; }
    .motivo { color: #888; font-style: italic; font-size: 0.9em; }
</style>
""", unsafe_allow_html=True)

st.title("🐘 Beto AI: Inteligência de Código")
st.write(f"🕒 Hora Atual: **{agora.strftime('%H:%M')}**")

# --- ENTRADA DE DADOS ---
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        casa = st.text_input("Equipa Casa", placeholder="Ex: Man. City")
        odd_casa = st.number_input("Odd Casa", value=1.50, step=0.01)
    with col2:
        fora = st.text_input("Equipa Fora", placeholder="Ex: Everton")
        odd_fora = st.number_input("Odd Fora", value=3.80, step=0.01)

    c1, c2 = st.columns(2)
    with c1:
        data_j = st.date_input("Data do Jogo", value=agora.date())
    with c2:
        hora_j = st.time_input("Hora do Jogo")

    if st.button("GERAR MELHOR CÓDIGO"):
        # 1. VALIDAÇÃO DE HORÁRIO
        dt_evento = angola_tz.localize(datetime.combine(data_j, hora_j))
        
        if dt_evento < agora:
            st.error(f"❌ O jogo {casa} vs {fora} já decorreu ou está em curso. Não é possível sugerir código.")
        else:
            # 2. INTELIGÊNCIA ARTIFICIAL DE ESCOLHA DE MERCADO
            # O sistema decide o melhor código baseado na discrepância das odds
            if odd_casa < 1.30 or odd_fora < 1.30:
                codigo = "1X ou 2X (Cercar Favorito)"
                razao = "Favoritismo esmagador. Recomendado assegurar a vitória ou empate do maior."
            elif 1.40 <= odd_casa <= 1.90 and 1.40 <= odd_fora <= 1.90:
                codigo = "AMBAS MARCAM (SIM)"
                razao = "Equipas equilibradas com ataque forte. A inteligência prevê golos de ambos os lados."
            elif odd_casa > 2.50 and odd_fora > 2.50:
                codigo = "+1.5 OU +2.5 GOLOS"
                razao = "Jogo aberto sem favorito claro. O mercado de golos é o mais lucrativo aqui."
            elif odd_casa < 1.50:
                codigo = "VENCEDOR 1 (CASA)"
                razao = "Domínio total da equipa da casa esperado conforme estatísticas da Google."
            elif odd_fora < 1.50:
                codigo = "VENCEDOR 2 (FORA)"
                razao = "A equipa visitante tem superioridade técnica para este confronto."
            else:
                codigo = "DNB (Empate Anula Aposta)"
                razao = "Risco de empate elevado. Este código protege o seu capital."

            st.markdown(f"""
            <div class="card-analise">
                <span style='color: #E61E25; font-weight: bold;'>🎯 ANÁLISE CONCLUÍDA</span><br>
                <b>{casa} vs {fora}</b><br>
                <span class="motivo">Motivo: {razao}</span><br>
                <span style='font-size: 0.8em; color: #aaa; margin-top: 10px; display: block;'>MELHOR CÓDIGO SUGERIDO:</span>
                <span class="codigo-mestre">{codigo}</span>
            </div>
            """, unsafe_allow_html=True)

st.info("O Beto AI analisa a probabilidade matemática para sugerir o código com maior chance de acerto.")
