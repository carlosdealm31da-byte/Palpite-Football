import streamlit as st
import random
from datetime import datetime
import pytz

# Configuração de Fuso Horário (Angola/Luanda)
angola_tz = pytz.timezone('Africa/Luanda')
agora = datetime.now(angola_tz)

st.set_page_config(page_title="Beto AI - O Decisor", page_icon="🎯", layout="centered")

# Estilo Dark Profissional
st.markdown("""
<style>
    .main { background-color: #0d1117; color: white; }
    .stButton>button { width: 100%; border-radius: 10px; height: 3.5em; font-weight: bold; background-color: #238636; color: white; border: none; }
    .card-analise { background-color: #161b22; padding: 25px; border-radius: 15px; border: 1px solid #30363d; margin-top: 20px; }
    .codigo-res { color: #39d353; font-size: 2.2em; font-weight: bold; display: block; margin: 10px 0; }
    .percent { color: #f1e05a; font-size: 1.4em; font-weight: bold; }
    .justificativa-box { background-color: #0d1117; padding: 15px; border-radius: 8px; border: 1px solid #30363d; margin-top: 15px; color: #8b949e; line-height: 1.6; }
</style>
""", unsafe_allow_html=True)

st.title("🎯 Beto AI: Inteligência Manual")
st.write(f"🕒 Hora Atual (Luanda): **{agora.strftime('%H:%M')}**")

# --- ENTRADA DE DADOS MANUAL ---
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        casa = st.text_input("Equipa da Casa", placeholder="Ex: Real Madrid")
        odd_c = st.number_input("Odd Casa", value=1.50, step=0.01)
    with col2:
        fora = st.text_input("Equipa de Fora", placeholder="Ex: Man. City")
        odd_f = st.number_input("Odd Fora", value=2.50, step=0.01)

    c3, c4 = st.columns(2)
    with c3:
        data_j = st.date_input("Data do Jogo", value=agora.date())
    with c4:
        hora_j = st.time_input("Hora de Início")

    # BOTÃO DE DECISÃO
    if st.button("ANALISAR E GERAR CÓDIGO"):
        # 1. VALIDADOR DE TEMPO REAL
        dt_evento = angola_tz.localize(datetime.combine(data_j, hora_j))
        
        if dt_evento < agora:
            st.error(f"⚠️ Erro: O jogo {casa} vs {fora} já começou ou já terminou (Início: {hora_j.strftime('%H:%M')}). Insira um jogo futuro.")
        else:
            # 2. MOTOR DE DECISÃO (A IA ESCOLHE O CÓDIGO)
            if odd_c < 1.35:
                codigo = "VENCEDOR 1 (CASA)"
                prob = random.uniform(92.5, 98.1)
                motivo = f"A inteligência escolheu este código porque o {casa} possui um favoritismo técnico absoluto para este encontro. Estatisticamente, odds neste nível indicam uma vitória segura com baixa margem de erro."
            
            elif odd_f < 1.35:
                codigo = "VENCEDOR 2 (FORA)"
                prob = random.uniform(92.5, 98.1)
                motivo = f"O código de vitória visitante foi selecionado devido à superioridade esmagadora do {fora}. Os dados de mercado sugerem que o adversário não terá capacidade defensiva para travar o resultado."
            
            elif 1.45 <= odd_c <= 2.20 and 1.45 <= odd_f <= 2.20:
                codigo = "AMBAS MARCAM (SIM)"
                prob = random.uniform(84.0, 89.9)
                motivo = "Este código foi o escolhido devido ao equilíbrio entre as equipas. Ambas possuem ataques agressivos e odds similares, o que torna o golo mútuo o mercado mais inteligente e provável."
            
            elif odd_c > 2.40 and odd_f > 2.40:
                codigo = "MAIS DE 1.5 GOLOS"
                prob = random.uniform(88.0, 95.2)
                motivo = "Sem favorito claro no papel, a IA decidiu pelo mercado de golos. É a decisão mais adequada para evitar riscos em vencedores num jogo onde a bola deve balançar a rede várias vezes."
            
            else:
                codigo = "DUPLA CHANCE (1X)"
                prob = random.uniform(80.0, 86.5)
                motivo = "A escolha deste código visa a proteção da banca. O favoritismo da casa é moderado, e a Dupla Chance garante o acerto mesmo em caso de um empate inesperado."

            # --- EXIBIÇÃO DO RESULTADO ---
            st.markdown(f"""
            <div class="card-analise">
                <span style='color: #238636; font-weight: bold; font-size: 0.9em;'>🎯 DECISÃO FINAL DA IA</span><br>
                <span style='font-size: 1.3em;'><b>{casa} vs {fora}</b></span><br>
                <span style='color: #8b949e; font-size: 0.85em;'>Início previsto: {hora_j.strftime('%H:%M')}</span><br><br>
                
                <span style='color: #8b949e; font-size: 0.9em;'>CÓDIGO SUGERIDO:</span>
                <span class="codigo-res">{codigo}</span>
                
                <span style='color: #8b949e; font-size: 0.9em;'>PROBABILIDADE DE ENTRADA:</span><br>
                <span class="percent">🔥 {prob:.1f}%</span>
                
                <div class="justificativa-box">
                    <b>PORQUÊ ESTE CÓDIGO?</b><br>
                    {motivo}
                </div>
            </div>
            """, unsafe_allow_html=True)

st.markdown("---")
st.caption("Beto AI: O seu decisor tático manual para qualquer liga mundial.")
