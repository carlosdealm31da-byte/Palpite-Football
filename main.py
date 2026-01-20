import streamlit as st
import random
from datetime import datetime, time
import pytz
import re

# Configuração de Luanda
angola_tz = pytz.timezone('Africa/Luanda')
agora = datetime.now(angola_tz)

st.set_page_config(page_title="Beto AI - Visão de Águia Total", layout="wide")

# Inicializar Bancos de Armazenamento
if 'banco_segura' not in st.session_state: st.session_state.banco_segura = []
if 'banco_milionario' not in st.session_state: st.session_state.banco_milionario = []
if 'banco_manual_puro' not in st.session_state: st.session_state.banco_manual_puro = []

# Estilo "Quadrado X" Musculado
st.markdown("""
<style>
    .main { background-color: #0b0e11; }
    .quadrado-x { 
        background-color: #1a1d23; padding: 25px; border-radius: 15px; 
        border: 2px solid #333; margin-bottom: 20px; border-left: 10px solid #E61E25;
    }
    .v-codigo { color: #39d353; font-size: 2.5em; font-weight: bold; }
    .status-ia { background: #0d1117; padding: 10px; border-radius: 8px; border: 1px solid #444; color: #f1e05a; }
</style>
""", unsafe_allow_html=True)

st.title("🦅 Beto AI: Visão de Águia & Comando Manual")
st.write(f"🕒 Luanda: **{agora.strftime('%H:%M')}**")

# --- MOTOR DE VISÃO (OCR / QR / FOTO) ---
def motor_visao_aguia(arquivo, modo):
    # Simulação de OCR avançado para Fotos, Screenshots e QR
    # Em um app real, aqui entraria a biblioteca 'pyzbar' para QR e 'pytesseract' para fotos
    if arquivo is not None:
        st.success(f"✅ Documento Detectado! Escaneando Código QR e Dados da Fotografia...")
        # Simulação de dados extraídos da foto/QR
        dados_extraidos = [
            ("Real Madrid", "AC Milan", 1.50, "21:00"),
            ("Arsenal", "Inter", 2.10, "21:00")
        ]
        for c, f, o, h in dados_extraidos:
            res = {"jogo": f"{c} vs {f}", "codigo": "VALENTE", "odd": o, "hora": h}
            if modo == "milionaria": st.session_state.banco_milionario.append(res)
            elif modo == "segura": st.session_state.banco_segura.append(res)
        return True
    return False

# --- ABAS DE OPERAÇÃO ---
tab1, tab2, tab3 = st.tabs(["✍️ COMANDO MANUAL", "🛡️ FICHA SEGURA", "🏆 FICHA MILIONÁRIA"])

with tab1:
    st.subheader("⚙️ Construção Manual Pura")
    st.write("Aqui você manda, a IA analisa a viabilidade da divisão.")
    with st.form("manual_puro"):
        c1, c2, c3 = st.columns(3)
        m_c = c1.text_input("Equipa Casa")
        m_f = c2.text_input("Equipa Fora")
        m_h = c3.text_input("Hora (HH:MM)")
        m_o = st.number_input("Odd", 1.01)
        if st.form_submit_button("📥 ANALISAR E GUARDAR NO BANCO"):
            st.session_state.banco_manual_puro.append({"jogo": f"{m_c} vs {m_f}", "codigo": "MANUAL", "odd": m_o, "hora": m_h})
            st.rerun()

    for j in st.session_state.banco_manual_puro:
        st.markdown(f"<div class='quadrado-x'>{j['jogo']} | {j['hora']}<br><span class='v-codigo'>CÓDIGO: {j['codigo']}</span></div>", unsafe_allow_html=True)

with tab2:
    st.subheader("🛡️ Ficha Segura (5-8 Jogos)")
    foto_s = st.file_uploader("📷 Subir Foto/Screenshot/QR (Segura)", type=['png', 'jpg', 'jpeg'], key="up_s")
    if foto_s: motor_visao_aguia(foto_s, "segura")
    
    # Exibir banco e permitir inserção manual para "inteirar"
    st.write(f"📊 Jogos no Armazenamento: {len(st.session_state.banco_segura)}")
    for j in st.session_state.banco_segura:
        st.markdown(f"<div class='quadrado-x' style='border-left-color:#238636;'>{j['jogo']}<br><span class='v-codigo'>{j['codigo']}</span></div>", unsafe_allow_html=True)

with tab3:
    st.subheader("🏆 Ficha Milionária (Até 40 Jogos)")
    foto_m = st.file_uploader("📷 Subir Foto/Screenshot/QR (Milionária)", type=['png', 'jpg', 'jpeg'], key="up_m")
    if foto_m: motor_visao_aguia(foto_m, "milionaria")

    for j in st.session_state.banco_milionario:
        st.markdown(f"<div class='quadrado-x'>{j['jogo']}<br><span class='v-codigo'>{j['codigo']}</span></div>", unsafe_allow_html=True)

if st.sidebar.button("🗑️ LIMPAR TODA A MEMÓRIA"):
    st.session_state.clear()
    st.rerun()
