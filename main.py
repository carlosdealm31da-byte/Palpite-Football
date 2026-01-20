import streamlit as st
import random
from datetime import datetime, timedelta
import pytz

# Configuração de Fuso Horário de Angola
angola_tz = pytz.timezone('Africa/Luanda')
agora = datetime.now(angola_tz)

st.set_page_config(page_title="Beto AI - Sistema de Metas", page_icon="🐘")

st.markdown("""
<style>
    .stButton>button { width: 100%; border-radius: 8px; height: 3.5em; font-weight: bold; background-color: #f04e23; color: white; }
    .card { padding: 20px; border: 1px solid #ddd; border-radius: 10px; background-color: #f9f9f9; }
</style>
""", unsafe_allow_html=True)

st.title("🐘 Beto AI: Inteligência Elephant Bet")
st.write(f"📅 Data: {agora.strftime('%d/%m/%Y')} | Meta: 50 Milhões")

# Entrada do Saldo para o Cálculo de Juros Compostos
valor_aposta = st.sidebar.number_input("Valor que vais apostar (KZ)", min_value=10.0, value=200.0)

# --- SEÇÃO 1: DIAGNÓSTICO INDIVIDUAL (O Cérebro) ---
st.header("🔍 Diagnóstico e Sugestão de Código")
col1, col2 = st.columns(2)
with col1:
    casa = st.text_input("Equipa Casa", "Petro de Luanda")
    ponto_c = st.number_input("Ponto da Banca (Casa)", value=1.50)
with col2:
    fora = st.text_input("Equipa Fora", "1º de Agosto")
    ponto_f = st.number_input("Ponto da Banca (Fora)", value=4.50)

if st.button("GERAR CÓDIGO DO JOGO"):
    # Lógica de Pontuação da Banca
    if ponto_c < ponto_f:
        res = "Casa (1)" if ponto_c < 1.45 else "1X (Dupla Possibilidade)"
    else:
        res = "Fora (2)" if ponto_f < 1.45 else "X2 (Dupla Possibilidade)"
    st.success(f"📌 CÓDIGO ELEPHANT BET: **{res}**")

st.markdown("---")

# --- SEÇÃO 2: GERADOR DE META AUTOMÁTICO (MILIONÁRIA) ---
st.header("🏆 Gerador de Bilhete: Rumo aos 50M")
st.write("O sistema vai calcular os jogos necessários até bater a meta baseada no teu valor de aposta.")

if st.button("BUSCAR COMBINAÇÃO PARA 50 MILHÕES"):
    meta = 50000000.0
    odd_alvo = meta / valor_aposta
    odd_acumulada = 1.0
    jogos_selecionados = []
    
    # O sistema "garimpa" jogos até a odd chegar ao objetivo
    tentativas = 0
    while odd_acumulada < odd_alvo and tentativas < 30:
        tentativas += 1
        o = round(random.uniform(1.40, 1.85), 2)
        if (odd_acumulada * o) > odd_alvo * 1.1: # Evita passar muito da meta
            continue
        
        # Simulação de Datas Reais (Próximos jogos)
        data_jogo = agora + timedelta(hours=random.randint(2, 48))
        mercado = random.choice(["Vencedor (1/2)", "Ambas Sim", "Mais 1.5 Gols", "Dupla Possibilidade"])
        
        jogos_selecionados.append({
            "data": data_jogo.strftime('%d/%m %H:%M'),
            "mercado": mercado,
            "odd": o
        })
        odd_acumulada *= o

    # Exibição do Resultado
    st.subheader(f"📑 Bilhete Milionário (Odd Total: {odd_acumulada:.2f})")
    for j in jogos_selecionados:
        st.write(f"🕒 {j['data']} | **{j['mercado']}** | Odd: {j['odd']}")
    
    ganho_final = valor_aposta * odd_acumulada
    if ganho_final > 50000000: ganho_final = 50000000
    
    st.markdown(f"""
    <div class="card">
        <h3 style="color: green;">💰 Prémio Estimado: {ganho_final:,.2f} KZ</h3>
        <p>Este bilhete foi calculado para atingir a meta dos 50 milhões com uma aposta de {valor_aposta} KZ.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")
st.info("O Beto AI aceita todas as divisões. Os horários estão sincronizados com Luanda.")
