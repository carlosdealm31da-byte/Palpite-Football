import streamlit as st
from scipy.stats import poisson

st.set_page_config(page_title="Beto AI - Estrategista 50M", page_icon="⚽")
st.title("⚽ Beto AI: Inteligência de Mercado")

# Entrada de Dados
col1, col2 = st.columns(2)
with col1:
    home_team = st.text_input("Time da Casa", "Kairat")
    home_mu = st.number_input(f"Média Gols: {home_team}", min_value=0.0, value=1.49, step=0.1)
with col2:
    away_team = st.text_input("Time de Fora", "Club Brugge")
    away_mu = st.number_input(f"Média Gols: {away_team}", min_value=0.0, value=1.0, step=0.1)

if st.button("FAZER DIAGNÓSTICO E SUGERIR CÓDIGO"):
    prob_home, prob_away, prob_draw = 0, 0, 0
    prob_btts, prob_over15, prob_over25 = 0, 0, 0
    
    for i in range(10):
        for j in range(10):
            p = poisson.pmf(i, home_mu) * poisson.pmf(j, away_mu)
            if i > j: prob_home += p
            elif i < j: prob_away += p
            else: prob_draw += p
            
            # Cálculo de outros mercados
            if i > 0 and j > 0: prob_btts += p
            if (i + j) > 1.5: prob_over15 += p
            if (i + j) > 2.5: prob_over25 += p

    st.markdown("---")
    st.subheader("📋 DIAGNÓSTICO DA IA")

    # LOGICA DE ESCOLHA DO CÓDIGO APROPRIADO
    if prob_home > 0.65:
        sugestao = f"Vitória Direta: {home_team}"
        codigo = "Casa (1)"
    elif prob_away > 0.65:
        sugestao = f"Vitória Direta: {away_team}"
        codigo = "Fora (2)"
    elif prob_over25 > 0.60:
        sugestao = "Jogo muito aberto (Gols)"
        codigo = "Mais de 2.5 Gols (Over 2.5)"
    elif prob_btts > 0.60:
        sugestao = "Ataques fortes, defesas fracas"
        codigo = "Ambas Marcam (Sim)"
    elif prob_home > 0.45 or prob_away > 0.45:
        fav = home_team if prob_home > prob_away else away_team
        sugestao = f"Equilíbrio com vantagem para {fav}"
        codigo = "Empate Anula a Aposta (DNB)"
    else:
        sugestao = "Jogo muito travado/difícil"
        codigo = "Menos de 2.5 Gols (Under 2.5)"

    st.success(f"📌 **SUGESTÃO:** {sugestao}")
    st.info(f"🎯 **CÓDIGO PARA USAR:** {codigo}")
    
    # Mostrar probabilidades detalhadas para conferência
    with st.expander("Ver detalhes do cálculo"):
        st.write(f"Chance de {home_team}: {prob_home*100:.1f}%")
        st.write(f"Chance de {away_team}: {prob_away*100:.1f}%")
        st.write(f"Chance de Ambas Marcam: {prob_btts*100:.1f}%")
