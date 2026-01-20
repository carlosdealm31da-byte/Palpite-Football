import streamlit as st
from scipy.stats import poisson

st.set_page_config(page_title="Beto AI - Meta 50M", page_icon="📈")
st.title("📈 Beto AI: Estrategista de Meta")

st.markdown("""
*Lógica da Banca: Valores baixos indicam maior força e favoritismo.*
""")

col1, col2 = st.columns(2)
with col1:
    home_team = st.text_input("Equipe Casa", "Kairat")
    home_score = st.number_input(f"Índice de Força {home_team}", min_value=0.1, value=1.2, step=0.1)
with col2:
    away_team = st.text_input("Equipe Fora", "Club Brugge")
    away_score = st.number_input(f"Índice de Força {away_team}", min_value=0.1, value=2.5, step=0.1)

if st.button("ANALISAR META E SUGERIR CÓDIGO"):
    # Invertendo a lógica para o cálculo: menor índice = maior média de sucesso
    mu_home = 3 / home_score 
    mu_away = 3 / away_score

    prob_home, prob_away, prob_draw = 0, 0, 0
    for i in range(10):
        for j in range(10):
            p = poisson.pmf(i, mu_home) * poisson.pmf(j, mu_away)
            if i > j: prob_home += p
            elif i < j: prob_away += p
            else: prob_draw += p

    st.markdown("---")
    
    # Diagnóstico Baseado na Meta
    if prob_home > prob_away and home_score < away_score:
        st.success(f"🎯 **CÓDIGO SUGERIDO:** Casa (1) ou Handicap 0")
        st.write(f"Análise: {home_team} tem o índice menor, logo maior probabilidade de bater a meta.")
    elif prob_away > prob_home and away_score < home_score:
        st.success(f"🎯 **CÓDIGO SUGERIDO:** Fora (2) ou Handicap 0")
        st.write(f"Análise: {away_team} é o favorito técnico pela pontuação da banca.")
    else:
        st.warning("⚠️ **CÓDIGO SUGERIDO:** Dupla Hipótese (1X ou X2)")
        st.write("Análise: Os índices estão equilibrados. Não arrisque vitória direta.")

    st.info(f"Probabilidade de Sucesso da Meta: {max(prob_home, prob_away)*100:.1f}%")
