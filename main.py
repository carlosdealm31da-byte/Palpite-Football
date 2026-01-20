import streamlit as st

st.set_page_config(page_title="Beto AI - Elephant Bet Edition", page_icon="🐘")
st.title("🐘 Beto AI: Consultor Elephant Bet Angola")

st.markdown("""
<style>
    .main { background-color: #f0f2f6; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #ff4b4b; color: white; }
</style>
""", unsafe_allow_html=True)

st.info("🎯 Estratégia focada para mercados da Elephant Bet")

col1, col2 = st.columns(2)
with col1:
    home_team = st.text_input("Equipa da Casa", "Petro de Luanda")
    home_odd = st.number_input(f"Odd na Elephant ({home_team})", value=1.80, step=0.01)
    
with col2:
    away_team = st.text_input("Equipa de Fora", "1º de Agosto")
    away_odd = st.number_input(f"Odd na Elephant ({away_team})", value=3.20, step=0.01)

if st.button("GERAR CÓDIGO ELEPHANT BET"):
    st.markdown("---")
    st.subheader("📋 BILHETE SUGERIDO (CÓDIGOS ANGOLA)")
    
    # Lógica de decisão baseada no padrão Elephant Bet
    if home_odd < 1.55:
        mercado = "Vencedor (1X2)"
        codigo_sugerido = f"Casa (1)"
        explicacao = f"A {home_team} é super favorita na Elephant Bet."
    elif away_odd < 1.55:
        mercado = "Vencedor (1X2)"
        codigo_sugerido = f"Fora (2)"
        explicacao = f"A {away_team} é super favorita na Elephant Bet."
    elif home_odd < 2.30 and away_odd < 2.30:
        mercado = "Ambas Equipas Marcam"
        codigo_sugerido = "Sim (BTTS)"
        explicacao = "Jogo equilibrado na nossa banda. Expectativa de golos de ambos lados."
    elif home_odd < 2.10:
        mercado = "Dupla Possibilidade"
        codigo_sugerido = "1X (Casa ou Empate)"
        explicacao = "Mais segurança para a tua caminhada dos 50M."
    else:
        mercado = "Total de Golos"
        codigo_sugerido = "Mais de 1.5"
        explicacao = "Mercado de segurança para evitar surpresas no vencedor."

    # Layout estilo bilhete de aposta
    st.success(f"📌 **MERCADO:** {mercado}")
    st.warning(f"🔢 **CÓDIGO NA ELEPHANT:** {codigo_sugerido}")
    st.write(f"💡 **PORQUÊ?** {explicacao}")
    
    st.markdown("---")
    st.write("📢 *Dica: Verifica sempre se a Elephant Bet não alterou a Odd antes de confirmares o teu bilhete.*")
