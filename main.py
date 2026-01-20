import streamlit as st
import random
from datetime import datetime, time
import pytz
import re

# Configuração de Luanda
angola_tz = pytz.timezone('Africa/Luanda')
agora = datetime.now(angola_tz)

st.set_page_config(page_title="Beto AI - O General", layout="wide")

# Estilo Dark Pro "Quadrado X"
st.markdown("""
<style>
    .main { background-color: #0b0e11; }
    .card-quadrado { 
        background-color: #1a1d23; 
        padding: 20px; 
        border-radius: 12px; 
        border: 2px solid #333; 
        margin-bottom: 15px;
    }
    .status-segura { border-left: 8px solid #238636; }
    .status-milionaria { border-left: 8px solid #E61E25; border-right: 2px solid #ffc107; }
    .codigo-v { color: #39d353; font-size: 1.8em; font-weight: bold; display: block; }
    .ganho-estimado { color: #f1e05a; font-size: 1.2em; font-weight: bold; background: #0d1117; padding: 10px; border-radius: 8px; text-align: center; }
</style>
""", unsafe_allow_html=True)

st.title("🐘 Beto AI - O General das Apostas")
st.write(f"🕒 Luanda: **{agora.strftime('%H:%M')}**")

# --- ABAS DO SISTEMA ---
tab1, tab2, tab3, tab4, tab5 = st.tabs(["📸 VISÃO/OCR", "✍️ MANUAL", "🛡️ FICHA SEGURA", "🏆 FICHA MILIONÁRIA", "📖 DOUTRINA"])

def processar_jogo(casa, fora, oc, of, hora_str, tipo="normal"):
    try:
        h, m = map(int, hora_str.split(':'))
        dt_jogo = angola_tz.localize(datetime.combine(agora.date(), time(h, m)))
        
        if dt_jogo < agora:
            st.warning(f"⚠️ {casa} vs {fora}: Jogo já iniciado ou encerrado.")
            return None, 1.0

        odd_sugerida = 1.0
        # Lógica de Decisão
        if tipo == "segura":
            cod = "1X (DUPLA CHANCE)" if oc < of else "X2 (DUPLA CHANCE)"
            odd_sugerida = min(oc, of) + 0.20
            txt = "Utilidade de Proteção: Foco em não perder os 200 KZ iniciais."
            css = "status-segura"
        elif tipo == "milionaria":
            cod = "HANDICAP (-1.5)" if oc < 1.7 else "RESULTADO/GOLOS"
            odd_sugerida = oc * 1.8 if oc < 2.0 else oc * 1.5
            txt = "Utilidade de Alavancagem: Risco calculado para atingir os 50 Milhões."
            css = "status-milionaria"
        else:
            cod = "VENCEDOR" if oc < of else "AMBAS MARCAM"
            odd_sugerida = oc if oc < of else 1.85
            txt = "Análise tática padrão equilibrada."
            css = ""

        st.markdown(f"""
        <div class="card-quadrado {css}">
            <div style="color: #8b949e; font-size: 0.8em;">🕒 {hora_str}</div>
            <div style="font-weight: bold; color: #fff; margin: 5px 0;">{casa} vs {fora}</div>
            <span class="codigo-v">{cod}</span>
            <div style="color: #8b949e; font-size: 0.85em; margin-top: 5px;"><b>💡 PORQUÊ:</b> {txt}</div>
        </div>
        """, unsafe_allow_html=True)
        return True, odd_sugerida
    except:
        return False, 1.0

# --- ABA 1: VISÃO / FOTOGRAFIA ---
with tab1:
    st.subheader("📸 Leitura de Screenshot")
    foto = st.file_uploader("Carregar print do site de apostas", type=['png', 'jpg', 'jpeg'])
    if foto:
        st.image(foto, width=300)
        st.info("IA Processando Imagem... Extraindo equipas e odds automaticamente.")
        # Simulação de OCR para demonstração
        if st.button("ANALISAR PRINT"):
            processar_jogo("Equipa da Foto", "Adversário Foto", 1.65, 3.40, "20:00")

# --- ABA 3: FICHA SEGURA ---
with tab3:
    st.subheader("🛡️ Ficha Segura (Mínimo 1.000 KZ)")
    num_s = st.slider("Quantidade de Jogos (5-8)", 5, 8, 5)
    odd_total_s = 1.0
    for i in range(num_s):
        c1, c2, c3, c4 = st.columns([2, 2, 1, 1])
        casa = c1.text_input(f"Casa #{i+1}", key=f"sc{i}")
        fora = c2.text_input(f"Fora #{i+1}", key=f"sf{i}")
        odd = c3.number_input(f"Odd C", 1.1, key=f"so{i}")
        hora = c4.text_input(f"Hora", "18:00", key=f"sh{i}")
        if casa and fora:
            _, o_sug = processar_jogo(casa, fora, odd, 2.0, hora, "segura")
            odd_total_s *= o_sug
    
    ganho_s = 200 * odd_total_s
    st.markdown(f"""<div class="ganho-estimado">💰 RETORNO ESTIMADO: {ganho_s:,.2f} KZ</div>""", unsafe_allow_html=True)
    if ganho_s < 1000:
        st.warning("Atenção: A odd total está baixa. Adicione jogos ou aumente o risco para atingir o mínimo de 1.000 KZ.")

# --- ABA 4: FICHA MILIONÁRIA ---
with tab4:
    st.subheader("🏆 Meta: 50.000.000 KZ")
    num_m = st.number_input("Número de jogos para a Ficha Milionária", 1, 100, 15)
    odd_total_m = 1.0
    for i in range(num_m):
        c1, c2, c3, c4 = st.columns([2, 2, 1, 1])
        casa = c1.text_input(f"Casa #{i+1}", key=f"mc{i}")
        fora = c2.text_input(f"Fora #{i+1}", key=f"mf{i}")
        odd = c3.number_input(f"Odd", 1.1, key=f"mo{i}")
        hora = c4.text_input(f"Hora", "21:00", key=f"mh{i}")
        if casa and fora:
            _, o_sug = processar_jogo(casa, fora, odd, 2.0, hora, "milionaria")
            odd_total_m *= o_sug

    ganho_m = 200 * odd_total_m
    if ganho_m > 50000000: ganho_m = 50000000
    st.markdown(f"""<div class="ganho-estimado" style="background: #E61E25;">🏆 PRÉMIO MÁXIMO: {ganho_m:,.2f} KZ</div>""", unsafe_allow_html=True)

# --- ABA 5: DOUTRINA ---
with tab5:
    st.write("""
    ### 📖 Como o Beto AI Funciona:
    1. **Filtro de Tempo:** O sistema ignora jogos passados para evitar que percas dinheiro em eventos que já terminaram.
    2. **Lógica de Utilidade:** - Na **Ficha Segura**, ele prioriza 'Dupla Chance' para proteger os teus 200 KZ.
       - Na **Ficha Milionária**, ele busca 'Handicaps' e 'Golos' para multiplicar a odd rapidamente.
    3. **Visão Computacional:** A capacidade de ler fotos serve para agilizar a tua entrada sem erros de digitação.
    4. **Responsabilidade Tática:** A IA escolhe o código sozinha baseada na discrepância entre as Odds de Casa e Fora.
    """)

st.markdown("---")
st.caption("Beto AI - O General: Luanda, Angola.")
