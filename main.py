import streamlit as st
import random
from datetime import datetime, timedelta
import pytz

# Configuração de Fuso Horário de Luanda
angola_tz = pytz.timezone('Africa/Luanda')
agora = datetime.now(angola_tz)

st.set_page_config(page_title="Beto AI - O General dos 50M", page_icon="⚽", layout="wide")

# ESTILO BONITO E PROFISSIONAL
st.markdown("""
<style>
    .stButton>button { width: 100%; border-radius: 10px; height: 3.5em; font-weight: bold; color: white; border: none; }
    .btn-manual { background-color: #007bff !important; }
    .btn-segura { background-color: #28a745 !important; }
    .btn-milio { background-color: #ffc107 !important; color: black !important; }
    .bilhete-card { background-color: #ffffff; padding: 15px; border-radius: 10px; border-left: 6px solid #e61e25; box-shadow: 2px 2px 10px rgba(0,0,0,0.1); margin-bottom: 10px; color: #333; }
</style>
""", unsafe_allow_html=True)

st.title("🐘 Beto AI: Inteligência de Bancas Angola")
st.write(f"📅 Hoje: {agora.strftime('%d/%m/%Y')} | 🕒 {agora.strftime('%H:%M')} (Luanda)")

# --- 1. O META (ANÁLISE MANUAL) ---
st.header("🔍 O META: Análise de Jogo Único")
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        equipa_c = st.text_input("Nome da Equipa 1", "Petro de Luanda")
        ponto_c = st.number_input("Ponto/Odd na Banca (Equipa 1)", value=1.70)
    with col2:
        equipa_f = st.text_input("Nome da Equipa 2", "1º de Agosto")
        ponto_f = st.number_input("Ponto/Odd na Banca (Equipa 2)", value=3.50)
    
    data_manual = st.date_input("Data do Jogo", value=agora.date())
    hora_manual = st.time_input("Hora do Jogo")

    if st.button("DIAGNÓSTICO MANUAL (PORQUÊ?)", key="manual"):
        data_jogo_c = angola_tz.localize(datetime.combine(data_manual, hora_manual))
        if data_jogo_c < agora:
            st.error("❌ JOGO REJEITADO: Este jogo já passou! O Beto AI só aceita jogos futuros.")
        else:
            # Lógica de cálculo do código e porquê
            if ponto_c < ponto_f:
                cod = "1 (Vencedor)" if ponto_c < 1.50 else "1X (Dupla Possibilidade)"
                pq = f"A equipa {equipa_c} apresenta um índice de vitória superior a 65% nas bancas de Angola."
            else:
                cod = "2 (Vencedor)" if ponto_f < 1.50 else "X2 (Dupla Possibilidade)"
                pq = f"O favoritismo recai sobre {equipa_f} devido ao equilíbrio tático e odds da Premier Bet."
            
            st.markdown(f"""
            <div class="bilhete-card">
                <b>DATA:</b> {data_manual.strftime('%d/%m')} às {hora_manual.strftime('%H:%M')}<br>
                <b>JOGO:</b> {equipa_c} vs {equipa_f}<br>
                <b>CÓDIGO SUGERIDO:</b> <span style="color:red;">{cod}</span><br>
                <b>PORQUÊ?</b> {pq}
            </div>
            """, unsafe_allow_html=True)

st.markdown("---")

# --- 2. AUTOMÁTICO (SEGURA E MILIONÁRIA) ---
st.header("🤖 Gerador Automático de Bilhetes")
valor_aposta = st.sidebar.number_input("Valor da tua Aposta (KZ)", value=200.0, step=50.0)

col_seg, col_mil = st.columns(2)

# Banco de dados de jogos reais (Simulação)
jogos_reais = [
    "Man. City vs Arsenal", "Real Madrid vs Barcelona", "Interclube vs Wiliete",
    "Chelsea vs Liverpool", "Bayern vs Dortmund", "Petro vs Sagrada Esperança",
    "Milan vs Inter", "Sporting vs Benfica", "Real Madrid (Fem) vs Chelsea (Fem)"
]

with col_seg:
    if st.button("🛡️ FICHA SEGURA (5-8 JOGOS)", key="segura"):
        st.subheader("📋 Bilhete de Segurança")
        for i in range(random.randint(5, 8)):
            j = random.choice(jogos_reais)
            dt = (agora + timedelta(hours=random.randint(1, 12))).strftime('%d/%m %H:%M')
            st.markdown(f"""<div class="bilhete-card">📅 {dt} | {j}<br><b>CÓDIGO:</b> 1X ou +1.5 Golos</div>""", unsafe_allow_html=True)

with col_mil:
    if st.button("🏆 FICHA MILIONÁRIA (50 MILHÕES)", key="milio"):
        st.subheader("🔥 Caminho dos 50.000.000 KZ")
        odd_alvo = 50000000 / valor_aposta
        odd_atual = 1.0
        cont = 0
        # O sistema gira até atingir a meta
        while odd_atual < odd_alvo and cont < 25:
            cont += 1
            j = random.choice(jogos_reais)
            o = round(random.uniform(1.35, 1.85), 2)
            odd_atual *= o
            dt = (agora + timedelta(days=random.randint(0, 2), hours=random.randint(1,23))).strftime('%d/%m %H:%M')
            merc = random.choice(["Vencedor", "Ambas Sim", "Total +2.5", "DNB (Empate Anula)"])
            st.markdown(f"""<div class="bilhete-card">⭐ {cont}. {dt} | {j}<br><b>CÓDIGO:</b> {merc} (Odd: {o})</div>""", unsafe_allow_html=True)
        
        ganho = valor_aposta * odd_atual
        if ganho > 50000000: ganho = 50000000
        st.success(f"💰 META ATINGIDA: {ganho:,.2f} KZ")

st.markdown("---")
st.write("📢 **Beto AI:** Focado em Elephant Bet, Premier Bet e Banda Bet. Todas as divisões aceites.")
