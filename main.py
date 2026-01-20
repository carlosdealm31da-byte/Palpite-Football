import streamlit as st
import pandas as pd
import numpy as np
from scipy.stats import poisson

# Configuração visual para celular
st.set_page_config(page_title="Beto AI - 50 Milhões", page_icon="⚽")

st.title("⚽ Beto AI: O Caminho dos 50 Milhões")
st.markdown("---")

# Motor de Cálculo Matemático
def calcular_previsao(media_casa, media_fora):
    prob_vitoria_casa = np.sum(np.triu(np.outer(
        poisson.pmf(range(6), media_casa), 
        poisson.pmf(range(6), media_fora)), 1))
    
    odd_justa = 1 / prob_vitoria_casa if prob_vitoria_casa > 0 else 0
    return prob_vitoria_casa, odd_justa

# Interface do Aplicativo
st.header("Analisar Novo Jogo")
time_casa = st.text_input("Time da Casa", "Ex: Flamengo")
time_fora = st.text_input("Time de Fora", "Ex: Vasco")

col_a, col_b = st.columns(2)
with col_a:
    g_casa = st.number_input(f"Média Gols {time_casa}", value=1.5)
with col_b:
    g_fora = st.number_input(f"Média Gols {time_fora}", value=1.0)

if st.button("CALCULAR PROBABILIDADE"):
    prob, odd = calcular_previsao(g_casa, g_fora)
    
    st.metric("Chance de Vitória", f"{prob:.1%}")
    st.metric("Odd Justa (Mínima)", f"{odd:.2f}")
    
    st.success(f"DICA: Só aposte se a odd da casa for MAIOR que {odd:.2f}")

st.markdown("---")
st.caption("Use com responsabilidade. Rumo aos 50 milhões!")
