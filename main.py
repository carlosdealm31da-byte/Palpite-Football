import streamlit as st
import random

# Configuração para evitar erros de CSS
st.markdown("""
<style>
    .codigo-res { color: #39d353; font-size: 2.2em; font-weight: bold; }
    .percent { color: #f1e05a; font-size: 1.4em; font-weight: bold; }
    .justificativa-box { background-color: #161b22; padding: 15px; border-radius: 8px; color: #8b949e; }
</style>
""", unsafe_allow_html=True)

# Entradas (Garanta que os nomes odd_c e odd_fora existem)
odd_c = st.number_input("Odd Casa", value=1.50)
odd_fora = st.number_input("Odd Fora", value=2.50)

if st.button("ANALISAR E GERAR CÓDIGO"):
    # Lógica de decisão
    if odd_c > 2.50 and odd_fora > 2.50:
        res = "DUPLA CHANCE"
        prob = "81.8%"
    else:
        res = "VENCEDOR"
        prob = "90.0%"

    # O SEGREDO: Usar markdown com unsafe_allow_html=True
    html_template = f"""
    <div style="background-color: #161b22; padding: 20px; border-radius: 10px;">
        <h3 style="color: #39d353;">🎯 DECISÃO FINAL DA IA</h3>
        <p style="color: #8b949e;">MELHOR CÓDIGO SUGERIDO:</p>
        <span class="codigo-res">{res}</span><br>
        <span class="percent">🔥 {prob}</span>
        <div class="justificativa-box">
            <b>PORQUÊ ESTE CÓDIGO?</b><br>
            A escolha deste código visa a proteção da banca baseada nas odds inseridas.
        </div>
    </div>
    """
    st.markdown(html_template, unsafe_allow_html=True)
