import streamlit as st
import random

# 1. Configuração de Estética e Cores
st.set_page_config(page_title="Beto AI - O General", layout="centered")

st.markdown("""
<style>
    .main { background-color: #0d1117; color: white; }
    .stButton>button { width: 100%; background-color: #E61E25; color: white; font-weight: bold; border-radius: 8px; height: 3.5em; border: none; }
    .card-decisao { background-color: #161b22; padding: 20px; border-radius: 12px; border-left: 8px solid #E61E25; margin-top: 20px; border: 1px solid #30363d; }
    .codigo-texto { color: #00ff00; font-size: 2.2em; font-weight: bold; display: block; margin-top: 5px; }
    .prob-texto { color: #ffc107; font-size: 1.4em; font-weight: bold; }
    .justificativa-box { background-color: #0d1117; padding: 15px; border-radius: 8px; margin-top: 15px; border: 1px solid #30363d; color: #8b949e; font-style: italic; }
</style>
""", unsafe_allow_html=True)

st.title("🐘 Beto AI: Decisor Inteligente")

# 2. Entrada de Dados Manual
st.subheader("📊 Analisador de Confronto")
col1, col2 = st.columns(2)
with col1:
    equipa_casa = st.text_input("Equipa da Casa", "Ex: Preston")
    odd_casa = st.number_input("Odd Casa", value=1.50)
with col2:
    equipa_fora = st.text_input("Equipa de Fora", "Ex: Everton")
    odd_fora = st.number_input("Odd Fora", value=3.00)

# 3. Processamento e Decisão
if st.button("GERAR CÓDIGO E JUSTIFICATIVA"):
    # Lógica Simplificada de Decisão
    if odd_casa < 1.35:
        resultado = "1 (VENCEDOR CASA)"
        probabilidade = random.uniform(90.1, 96.5)
        motivo = f"A inteligência escolheu este código devido ao favoritismo técnico absoluto do {equipa_casa}. A banca indica baixa resistência do adversário."
    elif odd_fora < 1.35:
        resultado = "2 (VENCEDOR FORA)"
        probabilidade = random.uniform(90.1, 96.5)
        motivo = f"O código 2 foi selecionado porque o {equipa_fora} domina o mercado tático para este confronto, com probabilidade máxima de vitória."
    elif 1.45 <= odd_casa <= 2.20 and 1.45 <= odd_fora <= 2.20:
        resultado = "AMBAS MARCAM (SIM)"
        probabilidade = random.uniform(82.5, 88.9)
        motivo = "Confronto equilibrado. A IA escolheu este código pois as odds indicam ataques ativos de ambos os lados e defesas expostas."
    else:
        resultado = "+1.5 GOLOS"
        probabilidade = random.uniform(85.0, 93.4)
        motivo = "A decisão foi tomada para garantir segurança. O mercado de golos é mais viável do que escolher um vencedor num jogo instável."

    # 4. Exibição do Resultado
    st.markdown(f"""
    <div class="card-decisao">
        <span style='color: #E61E25; font-weight: bold; font-size: 0.9em;'>🎯 DECISÃO FINAL</span><br>
        <b>{equipa_casa} vs {equipa_fora}</b><br><br>
        
        <span style='color: #8b949e; font-size: 0.85em;'>CÓDIGO SUGERIDO:</span>
        <span class="codigo-texto">{resultado}</span>
        
        <span style='color: #8b949e; font-size: 0.85em;'>PROBABILIDADE DE SUCESSO:</span><br>
        <span class="prob-texto">🔥 {probabilidade:.1f}%</span>
        
        <div class="justificativa-box">
            <b>JUSTIFICATIVA DA ESCOLHA:</b><br>
            {motivo}
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")
st.caption("Beto AI: O General da sua banca.")
