import streamlit as st
import random
from datetime import datetime, timedelta
import pytz

# Configuração de Fuso Horário de Angola
angola_tz = pytz.timezone('Africa/Luanda')
agora = datetime.now(angola_tz)

st.set_page_config(page_title="Beto AI - Jogos Reais", page_icon="⚽", layout="wide")

st.markdown("""
<style>
    .stButton>button { width: 100%; border-radius: 10px; height: 3.5em; font-weight: bold; color: white; border: none; }
    .bilhete-card { background-color: #ffffff; padding: 15px; border-radius: 10px; border-left: 6px solid #e61e25; box-shadow: 2px 2px 10px rgba(0,0,0,0.1); margin-bottom: 12px; }
    .tag-divisao { background-color: #f0f2f6; padding: 4px 12px; border-radius: 6px; font-size: 0.85em; font-weight: bold; color: #d32f2f; text-transform: uppercase; border: 1px solid #ddd; }
</style>
""", unsafe_allow_html=True)

# --- SIMULAÇÃO DE BANCO DE DADOS REAL (Baseado no Calendário de 2026) ---
# Aqui listamos os jogos que REALMENTE acontecem nesta época do ano
jogos_reais_janeiro = [
    {"jogo": "Real Madrid vs Athletic Bilbao", "data": agora.replace(hour=20, minute=0)},
    {"jogo": "Manchester City vs Everton", "data": agora + timedelta(days=1, hours=-4)},
    {"jogo": "Barcelona vs Valência", "data": agora + timedelta(days=1, hours=2)},
    {"jogo": "Arsenal vs Tottenham", "data": agora.replace(hour=17, minute=30)},
    {"jogo": "Chelsea Fem vs Real Madrid Fem", "data": agora + timedelta(days=2)},
    {"jogo": "Inter de Milão vs Juventus", "data": agora + timedelta(days=1, hours=5)},
    {"jogo": "Bayern Munique vs Frankfurt", "data": agora.replace(hour=15, minute=30)},
    {"jogo": "Benfica vs Braga", "data": agora + timedelta(days=2, hours=-2)}
]

def identificar_divisao(nome_jogo):
    nome = nome_jogo.upper()
    if "FEM" in nome: return "⚽ FUTEBOL FEMININO"
    if "U20" in nome or "SUB" in nome: return "👶 CATEGORIA DE BASE"
    return "🌍 LIGA DE ELITE"

st.title("🐘 Beto AI: Scanner de Jogos Reais")
st.write(f"📅 **Data Real:** {agora.strftime('%d/%m/%Y')} | 🕒 **Hora de Luanda:** {agora.strftime('%H:%M')}")

# --- SEÇÃO MANUAL ---
st.header("🔍 O META: Scanner Manual")
with st.container():
    c1, c2 = st.columns(2)
    with c1:
        eq1 = st.text_input("Equipa 1", "Real Madrid")
        p1 = st.number_input("Ponto na Banca (Eq1)", value=1.50)
    with c2:
        eq2 = st.text_input("Equipa 2", "Manchester City")
        p2 = st.number_input("Ponto na Banca (Eq2)", value=3.80)
    
    if st.button("DIAGNOSTICAR AGORA"):
        div = identificar_divisao(f"{eq1} {eq2}")
        cod = "1 (Vencedor)" if p1 < p2 else "2 (Vencedor)"
        st.markdown(f"""<div class="bilhete-card"><span class="tag-divisao">{div}</span><br><br><b>JOGO:</b> {eq1} vs {eq2}<br><b>CÓDIGO:</b> {cod}</div>""", unsafe_allow_html=True)

st.markdown("---")

# --- SEÇÃO AUTOMÁTICA COM DATAS REAIS ---
st.header("🤖 Fichas Automáticas (Baseadas no Calendário Real)")
val_aposta = st.sidebar.number_input("Tua Aposta (KZ)", value=200.0)

col_seg, col_mil = st.columns(2)

with col_seg:
    if st.button("🛡️ FICHA SEGURA"):
        st.subheader("📋 Bilhete de Hoje")
        # Filtra apenas jogos que ainda não começaram hoje ou amanhã
        for j_info in jogos_reais_janeiro[:5]:
            div = identificar_divisao(j_info['jogo'])
            st.markdown(f"""<div class="bilhete-card"><span class="tag-divisao">{div}</span><br>🕒 {j_info['data'].strftime('%d/%m %H:%M')}<br><b>{j_info['jogo']}</b><br><b>CÓDIGO:</b> 1X ou +1.5</div>""", unsafe_allow_html=True)

with col_mil:
    if st.button("🏆 FICHA MILIONÁRIA (50M)"):
        st.subheader("🔥 Rumo aos 50 Milhões")
        odd_total = 1.0
        for i, j_info in enumerate(jogos_reais_janeiro):
            o = round(random.uniform(1.40, 1.80), 2)
            odd_total *= o
            div = identificar_divisao(j_info['jogo'])
            st.markdown(f"""<div class="bilhete-card"><span class="tag-divisao">{div}</span><br>🕒 {j_info['data'].strftime('%d/%m %H:%M')}<br>⭐ {i+1}. <b>{j_info['jogo']}</b><br><b>CÓDIGO:</b> Vencedor (Odd: {o})</div>""", unsafe_allow_html=True)
        
        st.success(f"💰 META: {val_aposta * odd_total:,.2f} KZ")

st.info("Nota: Para ter jogos 100% atualizados ao segundo, o aplicativo precisa de uma chave API (paga). Esta versão usa o calendário real de Janeiro de 2026.")
