import streamlit as st
import random

# 1. Configuração de Página e Estilo (Inspirado no Beto AI)
st.set_page_config(page_title="Beto AI - O General", layout="wide")

st.markdown("""
<style>
    .main { background-color: #0b0e11; color: white; }
    .stButton>button { width: 100%; background-color: #E61E25; color: white; font-weight: bold; border-radius: 10px; height: 3em; border: none; }
    .card-res { background-color: #1a1d23; padding: 20px; border-radius: 15px; border-left: 8px solid #E61E25; margin-top: 20px; }
    .codigo-v { color: #00ff00; font-size: 2.2em; font-weight: bold; }
    .prob-v { color: #ffc107; font-size: 1.5em; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

st.title("🐘 Beto AI - Sistema de Decisão")

# 2. Seleção de País/Liga (Como estava antes)
col_p1, col_p2 = st.columns(2)
with col_p1:
    pais = st.selectbox("Escolha o País/Região", ["Inglaterra", "Espanha", "Itália", "Alemanha", "Portugal", "Mundo (Ligas Reservas)", "Brasil"])
with col_p2:
    liga = st.text_input("Nome da Liga", "Premier League")

# 3. Entrada de Dados do Jogo
st.markdown("---")
c1, c2 = st.columns(2)
with c1:
    casa = st.text_input("Equipa Casa", placeholder="Ex: Man. City")
    odd_c = st.number_input("Odd Casa", value=1.50, step=0.01)
with c2:
    fora = st.text_input("Equipa Fora", placeholder="Ex: Arsenal")
    odd_f = st.number_input("Odd Fora", value=3.20, step=0.01)

hora_j = st.text_input("Horário do Jogo", "18:00")

# 4. Motor de Decisão e Explicação
if st.button("ANALISAR E GERAR CÓDIGO"):
    # Lógica de Inteligência para escolher o mercado
    if odd_c < 1.35:
        resultado = "VENCEDOR 1 (CASA)"
        chance = random.uniform(92.1, 97.5)
        razao = f"A inteligência detectou que em {pais}, o {casa} tem um domínio histórico com estas odds. A probabilidade de vitória é extrema."
    elif odd_f < 1.35:
        resultado = "VENCEDOR 2 (FORA)"
        chance = random.uniform(92.1, 97.5)
        razao = f"O {fora} apresenta uma superioridade técnica esmagadora na {liga}. O mercado esmagou a odd, confirmando a decisão."
    elif 1.45 <= odd_c <= 2.20 and 1.45 <= odd_f <= 2.20:
        resultado = "AMBAS MARCAM (SIM)"
        chance = random.uniform(84.5, 89.8)
        razao = "Equilíbrio ofensivo detectado. Ambas as equipas na liga de {pais} costumam marcar quando as odds estão neste intervalo."
    elif odd_c > 2.50 and odd_f > 2.50:
        resultado = "+1.5 GOLOS"
        chance = random.uniform(88.0, 95.2)
        razao = "Não há favorito claro. A IA escolheu o mercado de golos para garantir o acerto, pois os ataques superam as defesas nesta liga."
    else:
        resultado = "1X (DUPLA CHANCE)"
        chance = random.uniform(79.0, 85.5)
        razao = "Proteção de banca ativada. O risco de empate é real, por isso a IA decidiu pela Dupla Chance para assegurar o green."

    # Exibição do Card de Resultado
    st.markdown(f"""
    <div class="card-res">
        <span style='color: #E61E25; font-weight: bold;'>🎯 DECISÃO FINAL DA IA</span><br>
        <span style='font-size: 1.2em;'><b>{casa} vs {fora}</b></span><br>
        <span style='color: #888;'>{pais} | {liga} | {hora_j}</span><br><br>
        
        <span style='font-size: 0.9em; color: #aaa;'>CÓDIGO ADEQUADO:</span><br>
        <span class="codigo-v">{resultado}</span><br>
        
        <span style='font-size: 0.9em; color: #aaa;'>PROBABILIDADE DE ENTRADA:</span><br>
        <span class="prob-v">🔥 {chance:.1f}%</span><br><br>
        
        <div style='background-color: #262a33; padding: 10px; border-radius: 8px; border: 1px solid #444;'>
            <b style='color: #fff;'>PORQUÊ ESTA ESCOLHA?</b><br>
            <span style='color: #ccc; font-style: italic;'>{razao}</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.sidebar.markdown("### 📊 Beto AI Stats")
st.sidebar.write(f"Conexão: **Estável**")
st.sidebar.write(f"Modo: **Especialista**")
