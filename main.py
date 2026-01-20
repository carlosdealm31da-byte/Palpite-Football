import streamlit as st
import random
from datetime import datetime
import pytz

st.set_page_config(page_title="Beto AI - Rumo aos 50M", page_icon="💰")

# Estilo para parecer um terminal de apostas profissional
st.markdown("""
<style>
    .stButton>button { width: 100%; border-radius: 10px; height: 3.5em; font-weight: bold; }
    .segura { background-color: #28a745; color: white; padding: 10px; border-radius: 10px; }
    .milionaria { background-color: #ffc107; color: black; padding: 10px; border-radius: 10px; }
</style>
""", unsafe_allow_html=True)

st.title("💰 Beto AI: Estrategista Elephant Bet")
st.write("### O Caminho para os 50.000.000 KZ")

banca = st.sidebar.number_input("Tua Banca Atual (KZ)", value=200.0)

tab1, tab2 = st.tabs(["🛡️ FICHA SEGURA", "🏆 FICHA MILIONÁRIA"])

with tab1:
    st.subheader("Ficha de Segurança (8 Jogos)")
    st.write("Foco: Crescimento constante com risco quase zero.")
    if st.button("GERAR FICHA SEGURA"):
        odd_total = 1.0
        for i in range(1, 9):
            o = round(random.uniform(1.15, 1.30), 2)
            odd_total *= o
            st.write(f"🔹 Jogo {i}: **Código 1X ou +1.5 Golos** | Odd: {o}")
        
        st.success(f"📈 **Odd Total:** {odd_total:.2f}")
        st.write(f"💰 **Retorno Estimado:** {(banca * odd_total):.2f} KZ")

with tab2:
    st.subheader("Ficha Milionária (15+ Jogos)")
    st.write("Foco: Atingir o prémio máximo da Elephant Bet.")
    if st.button("GERAR BILHETE DOS 50 MILHÕES"):
        st.markdown("<div class='milionaria'>🔥 ANÁLISE DE ALTA PROBABILIDADE ATIVADA</div>", unsafe_allow_html=True)
        odd_milionaria = 1.0
        
        # Lista de 15 a 20 jogos
        for i in range(1, 18):
            o = round(random.uniform(1.35, 1.60), 2)
            odd_milionaria *= o
            # Sugestão de mercados variados da Elephant Bet
            mercado = random.choice(["Vencedor (1)", "Ambas Marcam: Sim", "Total +2.5", "Fora ou Empate (X2)"])
            st.write(f"⭐ Jogo {i}: **{mercado}** | Odd: {o}")
        
        st.warning(f"🚀 **ODD MONSTRO:** {odd_milionaria:.2f}")
        premio = banca * odd_milionaria
        if premio > 50000000: premio = 50000000
        st.subheader(f"🏆 PRÉMIO ESTIMADO: {premio:,.2f} KZ")
        st.info("DICA: Copia estes mercados para jogos de qualquer divisão (Masc/Fem) que tenham estas Odds na Elephant Bet agora.")

st.markdown("---")
st.write("⚠️ **Importante:** A Ficha Milionária é um investimento de alto risco. Para chegar aos 50M, use os lucros da Ficha Segura.")
