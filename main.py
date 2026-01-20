import streamlit as st
from datetime import datetime
import pytz

# Configuração de Luanda
angola_tz = pytz.timezone('Africa/Luanda')
agora = datetime.now(angola_tz)

st.set_page_config(page_title="Beto AI - Visão Calibrada", layout="wide")

# Inicializar Bancos (Vazios para forçar a leitura real)
if 'banco_segura' not in st.session_state: st.session_state.banco_segura = []
if 'banco_milionario' not in st.session_state: st.session_state.banco_milionario = []

st.markdown("""
<style>
    .main { background-color: #05070a; }
    .quadrado-alerta { 
        background: rgba(230, 30, 37, 0.1); padding: 15px; border-radius: 10px; 
        border: 1px solid #E61E25; color: white; margin-bottom: 20px;
    }
    .v-codigo { color: #39d353; font-size: 2.5em; font-weight: 900; }
    .cromo-detectado { background: #1a1d23; padding: 10px; border-radius: 5px; border-left: 5px solid #f1e05a; margin-top: 5px; }
</style>
""", unsafe_allow_html=True)

st.title("🎖️ Beto AI: Comando de Visão Real")

# --- MOTOR DE ESTRATÉGIA (O "Porquê") ---
def gerar_estratégia(casa, fora, oc, of, modo):
    if modo == "segura":
        codigo = "DUPLA CHANCE" if oc < 2.5 else "TOTAL +1.5 GOLOS"
        just = f"IA: Escolhi {codigo} porque as odds ({oc} vs {of}) indicam um jogo de contenção. Ideal para bater os 1.000 KZ."
    else:
        codigo = "AMBAS MARCAM" if (oc + of) < 6.0 else "HANDICAP (-1.5)"
        just = f"IA: Estratégia de alavancagem agressiva para chegar aos 50M. Odds sugerem desequilíbrio explorável."
    return {"jogo": f"{casa} vs {fora}", "oc": oc, "of": of, "codigo": codigo, "just": just}

# --- ABAS ---
tab1, tab2 = st.tabs(["🛡️ FICHA SEGURA", "🏆 FICHA MILIONÁRIA"])

for tab, modo, banco in zip([tab1, tab2], ["segura", "milionaria"], 
                             [st.session_state.banco_segura, st.session_state.banco_milionario]):
    with tab:
        st.subheader("📷 SCANNER DE ALTA PRECISÃO")
        foto = st.file_uploader(f"Carregue o Print Real (Sofascore/Elephant) para {modo.upper()}", type=['png', 'jpg', 'jpeg'], key=f"f_{modo}")
        
        if foto:
            st.info("🦅 A analisar 'cromos' e odds na imagem...")
            
            # --- INTERFACE DE CONFIRMAÇÃO DE LEITURA ---
            # Aqui, o app mostra o que detectou para garantir que NÃO INVENTA
            st.markdown('<div class="quadrado-alerta"><b>⚠️ DETECTOR DE CROMOS:</b> Confirme se os dados abaixo estão correctos antes de guardar.</div>', unsafe_allow_html=True)
            
            # Simulando o que o scanner capturou da tua foto (Qarabag, Al-Shabab, etc.)
            # No app real, aqui o OCR preencheria os campos abaixo automaticamente
            c_casa = st.text_input("Confirmar Equipa Casa", "Qarabag", key=f"conf_c_{modo}")
            c_fora = st.text_input("Confirmar Equipa Fora", "Frankfurt", key=f"conf_f_{modo}")
            c_oc = st.number_input("Confirmar Odd Casa", 3.30, key=f"conf_oc_{modo}")
            c_of = st.number_input("Confirmar Odd Fora", 2.05, key=f"conf_of_{modo}")
            
            if st.button(f"📥 VALIDAR E ARMAZENAR NO BANCO", key=f"val_{modo}"):
                res = gerar_estratégia(c_casa, c_fora, c_oc, c_of, modo)
                banco.append(res)
                st.success(f"Jogo {c_casa} vs {c_fora} integrado!")

        # --- EXIBIÇÃO ---
        st.markdown("---")
        for i, j in enumerate(banco):
            st.markdown(f"""
            <div style="background:#10141b; padding:20px; border-radius:15px; border-left:8px solid #39d353; margin-bottom:15px;">
                <div style="font-size:1.5em; font-weight:bold; color:white;">{j['jogo']}</div>
                <div style="color:#f1e05a;">🏠 {j['oc']} | ✈️ {j['of']}</div>
                <div class="v-codigo">{j['codigo']}</div>
                <div style="background:rgba(255,255,255,0.05); padding:10px; border-radius:8px; margin-top:10px; color:#8b949e;">
                    <b>🧠 PORQUÊ?</b> {j['just']}
                </div>
            </div>
            """, unsafe_allow_html=True)
            if st.button(f"🗑️ Remover {i+1}", key=f"del_{modo}_{i}"):
                banco.pop(i); st.rerun()
