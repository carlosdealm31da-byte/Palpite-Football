import streamlit as st
from scipy.stats import poisson

st.set_page_config(page_title="Beto AI - Estratégia 50M", page_icon="⚽")

st.title("⚽ Beto AI: O Caminho dos 50 Milhões")
st.markdown("---")

# Entradas de dados
col1, col2 = st.columns(2)
with col1:
    home_team = st.text_input("Time da Casa", "Kairat")
    home_mu = st.number_input(f"Média de Gols: {home_team}", min_value=0.0, value=1.49, step=0.1)

with col2:
    away_team = st.text_input("Time de Fora", "Club Brugge")
    away_mu = st.number_input(f"Média de Gols: {away_team}", min_value=0.0, value=1.0, step=0.1)

if st.button("GERAR DIAGNÓSTICO REALISTA"):
    # Cálculo de Probabilidades usando Poisson
    prob_home = 0
    prob_away = 0
    prob_draw = 0
    
    for i in range(10): # Gols do time da casa
        for j in range(10): # Gols do time de fora
            p = poisson.pmf(i, home_mu) * poisson.pmf(j, away_mu)
            if i > j:
                prob_home += p
            elif i < j:
                prob_away += p
            else:
                prob_draw += p

    # Exibição dos Resultados
    st.subheader("📊 Probabilidades Reais")
    c1, c2, c3 = st.columns(3)
    c1.metric(home_team, f"{prob_home*100:.1f}%")
    c2.metric("Empate", f"{prob_draw*100:.1f}%")
    c3.metric(away_team, f"{prob_away*100:.1f}%")

    st.markdown("---")
    
    # Cálculo das Odds Justas
    odd_h = 1/prob_home if prob_home > 0 else 100
    odd_d = 1/prob_draw if prob_draw > 0 else 100
    odd_a = 1/prob_away if prob_away > 0 else 100

    st.subheader("💰 Tabela de Odds Justas (Mínimas)")
    st.write(f"**{home_team}:** {odd_h:.2f} | **Empate:** {odd_d:.2f} | **{away_team}:** {odd_a:.2f}")
    
    st.success(f"💡 DICA: Só aposte se a banca pagar MAIS do que os valores acima!")
