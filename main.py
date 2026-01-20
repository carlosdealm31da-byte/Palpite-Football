import streamlit as st
import random
from datetime import datetime, time
import pytz

# Configuração de Luanda
angola_tz = pytz.timezone('Africa/Luanda')
agora = datetime.now(angola_tz)

st.set_page_config(page_title="Beto AI - Sistema de Odds Total", layout="wide")

# Inicializar Bancos
if 'banco_segura' not in st.session_state: st.session_state.banco_segura = []
if 'banco_milionario' not in st.session_state: st.session_state.banco_milionario = []

st.markdown("""
<style>
    .main { background-color: #0b0e11; }
    .quadrado-x { 
        background-color: #1a1d23; padding: 25px; border-radius: 15px; 
        border: 2px solid #333; margin-bottom: 20px; border-left: 10px solid #E61E25;
    }
    .v-codigo { color: #39d353; font-size: 2.3em; font-weight: bold; }
    .caixa-porque { 
        background-color: #0d1117; padding: 15px; border-radius: 10px; 
        border: 1px solid #444; color: #f1e05a; font-size: 0.95em;
    }
    .display-odds { color: #8b949e; font-weight: bold; margin-bottom: 10px; }
</style>
""", unsafe_allow_html=True)

st.title("🦅 Beto AI: Visão de Águia (ODDS CASA/FORA)")
st.write(f"🕒 Central Luanda: **{agora.strftime('%H:%M')}**")

# --- MOTOR DE JUSTIFICATIVA COM ANÁLISE DE ODDS ---
def processar_estrategia(casa, fora, o_casa, o_fora, hora, modo):
    # IA decide o código baseado na comparação das Odds (Dedés)
    if modo == "segura":
        # Se as odds forem próximas, vai no mercado de golos
        if abs(o_casa - o_fora) < 0.5:
            codigo = "TOTAL +1.5 GOLOS"
            pq = f"Análise: Equipes equilibradas (Casa {o_casa} | Fora {o_fora}). O risco de empate é alto, por isso foquei no volume de golos para garantir a meta de 1.000 KZ."
        else:
            codigo = "DUPLA CHANCE"
            pq = f"Análise: Há um favorito claro. Cobrimos dois resultados para manter a segurança da ficha."
    else: # Milionária
        codigo = "HANDICAP (-1.5)" if o_casa < o_fora else "AMBAS MARCAM & +2.5"
        pq = f"Análise Milionária: Com Odd Casa {o_casa} vs Fora {o_fora}, a IA detectou uma oportunidade de alavancagem agressiva para os 50M."

    return {
        "jogo": f"{casa} vs {fora}",
        "o_casa": o_casa,
        "o_fora": o_fora,
        "codigo": codigo,
        "just": pq,
        "hora": hora,
        "odd_calculo": min(o_casa, o_fora) * 1.5 # Simulação de prémio
    }

# --- ABAS ---
tab1, tab2 = st.tabs(["🛡️ FICHA SEGURA", "🏆 FICHA MILIONÁRIA"])

for tab, modo, banco, cor in zip([tab1, tab2], ["segura", "milionaria"], 
                                 [st.session_state.banco_segura, st.session_state.banco_milionario],
                                 ["#238636", "#E61E25"]):
    with tab:
        # 1. VISÃO DE ÁGUIA (LEITURA DE FOTO/QR)
        st.subheader(f"📷 Scanner {modo.upper()}")
        foto = st.file_uploader(f"Subir imagem para {modo.capitalize()}", type=['png', 'jpg'], key=f"f_{modo}")
        
        if foto and st.button(f"🦅 LER E ANALISAR ODDS", key=f"s_{modo}"):
            # Simulação: IA extraindo Odds de Casa e Fora da foto
            lidos = [("Real Madrid", "AC Milan", 1.50, 5.80, "21:00")]
            for c, f, oc, of, h in lidos:
                res = processar_estrategia(c, f, oc, of, h, modo)
                banco.append(res)
            st.rerun()

        # 2. MODO MANUAL INTEGRADO (COM AS DUAS ODDS)
        with st.expander("➕ INSERÇÃO MANUAL (CASA/FORA)"):
            c1, c2 = st.columns(2)
            mc = c1.text_input("Equipa Casa", key=f"mc_{modo}")
            mf = c2.text_input("Equipa Fora", key=f"mf_{modo}")
            c3, c4, c5 = st.columns(3)
            oc = c3.number_input("Odd Casa", 1.01, key=f"oc_{modo}")
            of = c4.number_input("Odd Fora", 1.01, key=f"of_{modo}")
            mh = c5.text_input("Hora", "20:00", key=f"mh_{modo}")
            
            if st.button("📥 GUARDAR NO ARMAZENAMENTO", key=f"bm_{modo}"):
                res = processar_estrategia(mc, mf, oc, of, mh, modo)
                banco.append(res); st.rerun()

        # 3. EXIBIÇÃO DO BANCO
        st.markdown("---")
        for i, j in enumerate(banco):
            st.markdown(f"""
            <div class="quadrado-x" style="border-left-color: {cor}">
                <small>🕒 {j['hora']} | JOGO {i+1}</small>
                <div style="font-size:1.4em; font-weight:bold; color:white;">{j['jogo']}</div>
                <div class="display-odds">🏠 CASA: {j['o_casa']} | ✈️ FORA: {j['o_fora']}</div>
                <span class="v-codigo">{j['codigo']}</span>
                <div class="caixa-porque"><b>🧠 ESTRATÉGIA IA:</b><br>{j['just']}</div>
            </div>
            """, unsafe_allow_html=True)
            if st.button(f"🗑️ Remover {i+1}", key=f"del_{modo}_{i}"):
                banco.pop(i); st.rerun()

if st.sidebar.button("🗑️ LIMPAR TUDO"):
    st.session_state.clear()
    st.rerun()
