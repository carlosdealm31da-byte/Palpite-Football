import streamlit as st
import random
from datetime import datetime, time
import pytz

# Configuração de Luanda
angola_tz = pytz.timezone('Africa/Luanda')
agora = datetime.now(angola_tz)

st.set_page_config(page_title="Beto AI - Premium", layout="wide")

# Inicializar Bancos
if 'banco_segura' not in st.session_state: st.session_state.banco_segura = []
if 'banco_milionario' not in st.session_state: st.session_state.banco_milionario = []

# --- ESTÉTICA PREMIUM (EMBELEZAMENTO TOTAL) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap');
    
    html, body, [class*="st-"] { font-family: 'Inter', sans-serif; background-color: #05070a; }
    
    /* Quadrado X Estilo Glassmorphism */
    .quadrado-premium { 
        background: linear-gradient(145deg, #10141b, #0d0f14);
        padding: 25px; 
        border-radius: 20px; 
        border: 1px solid rgba(255, 255, 255, 0.05);
        margin-bottom: 25px; 
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
        transition: transform 0.3s ease;
    }
    .quadrado-premium:hover { transform: translateY(-5px); border: 1px solid rgba(57, 211, 83, 0.3); }
    
    /* Tipografia e Cores */
    .v-codigo { 
        background: linear-gradient(90deg, #39d353, #2ea043);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 2.8em; font-weight: 900; letter-spacing: -1px;
    }
    .badge-odds { background: #1a1d23; color: #f1e05a; padding: 5px 12px; border-radius: 8px; font-weight: bold; font-size: 0.9em; border: 1px solid #333; }
    .justificativa-box { background: rgba(0,0,0,0.3); padding: 15px; border-radius: 12px; border-left: 4px solid #39d353; color: #8b949e; font-size: 0.95em; }
    
    /* Cabeçalho de Status */
    .header-info { background: linear-gradient(90deg, #0d1117, #161b22); padding: 20px; border-radius: 15px; border: 1px solid #30363d; margin-bottom: 30px; text-align: center; }
</style>
""", unsafe_allow_html=True)

# --- CABEÇALHO ---
st.markdown(f"""
<div class="header-info">
    <h1 style="margin:0; color:white; font-weight:900;">🦅 BETO AI <span style="color:#E61E25;">V3</span></h1>
    <p style="margin:5px 0 0 0; color:#8b949e;">LUANDA, ANGOLA | <b>{agora.strftime('%H:%M')}</b></p>
</div>
""", unsafe_allow_html=True)

# --- MOTOR DE INTELIGÊNCIA ---
def analisar_missao(casa, fora, oc, of, hora, modo):
    if modo == "segura":
        codigo = "DUPLA CHANCE" if abs(oc-of) > 0.4 else "TOTAL +1.5 GOLOS"
        tipo = "PROTEÇÃO DE CAPITAL"
    else:
        codigo = "HANDICAP (-1.5)" if oc < of else "AMBAS MARCAM & +2.5"
        tipo = "ALAVANCAGEM MILIONÁRIA"
    
    just = f"Análise Beto AI: Confronto detectado entre {casa} ({oc}) e {fora} ({of}). Decidi pelo código {codigo} pois a estrutura das odds indica uma zona de {tipo}. Apto para armazenamento imediato."
    return {"jogo": f"{casa} vs {fora}", "oc": oc, "of": of, "codigo": codigo, "just": just, "hora": hora, "odd": oc if oc < of else of}

# --- INTERFACE DE COMANDO ---
tab1, tab2 = st.tabs(["🛡️ FICHA SEGURA (SEM LIMITES)", "🏆 FICHA MILIONÁRIA (50M)"])

for tab, modo, banco, cor in zip([tab1, tab2], ["segura", "milionaria"], 
                                 [st.session_state.banco_segura, st.session_state.banco_milionario],
                                 ["#238636", "#E61E25"]):
    with tab:
        # Área de Entrada (Manual e Visão)
        c1, c2 = st.columns([1, 1])
        with c1:
            with st.expander("➕ COMANDO MANUAL", expanded=False):
                ec = st.text_input("Casa", key=f"c_{modo}")
                ef = st.text_input("Fora", key=f"f_{modo}")
                col_o1, col_o2, col_h = st.columns(3)
                eo1 = col_o1.number_input("Odd Casa", 1.01, key=f"o1_{modo}")
                eo2 = col_o2.number_input("Odd Fora", 1.01, key=f"o2_{modo}")
                eh = col_h.text_input("Hora", "20:00", key=f"h_{modo}")
                if st.button("📥 GUARDAR NO BANCO", key=f"btn_{modo}"):
                    st.session_state[f"banco_{modo}"].append(analisar_missao(ec, ef, eo1, eo2, eh, modo))
                    st.rerun()
        
        with c2:
            foto = st.file_uploader("📷 VISÃO DE ÁGUIA (FOTO/QR)", type=['png', 'jpg'], key=f"img_{modo}")
            if foto and st.button("🦅 ESCANEAR IMAGEM", key=f"scan_{modo}"):
                # Simulação de leitura avançada
                st.session_state[f"banco_{modo}"].append(analisar_missao("Real Madrid", "AC Milan", 1.50, 5.80, "21:00", modo))
                st.rerun()

        # Listagem dos Jogos com Estética Premium
        st.markdown("---")
        for i, j in enumerate(banco):
            st.markdown(f"""
            <div class="quadrado-premium" style="border-left: 8px solid {cor};">
                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;">
                    <span style="color:#8b949e; font-size:0.8em; font-weight:bold;">🕒 {j['hora']} | MISSÃO {i+1}</span>
                    <div>
                        <span class="badge-odds">CASA: {j['oc']}</span>
                        <span class="badge-odds">FORA: {j['of']}</span>
                    </div>
                </div>
                <div style="font-size:1.8em; font-weight:900; color:white; margin-bottom:5px;">{j['jogo']}</div>
                <div class="v-codigo">{j['codigo']}</div>
                <div class="justificativa-box">
                    <b>🧠 JUSTIFICATIVA TÁTICA:</b><br>{j['just']}
                </div>
            </div>
            """, unsafe_allow_html=True)
            if st.button(f"🗑️ EXCLUIR JOGO {i+1}", key=f"del_{modo}_{i}"):
                banco.pop(i)
                st.rerun()

# Sidebar de Limpeza
if st.sidebar.button("🚨 REINICIAR SISTEMA"):
    st.session_state.clear()
    st.rerun()
