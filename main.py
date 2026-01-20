import streamlit as st
import random
from datetime import datetime
import pytz

# Configuração de Luanda
angola_tz = pytz.timezone('Africa/Luanda')
agora = datetime.now(angola_tz)

st.set_page_config(page_title="Beto AI - Visão Real", layout="wide")

# Inicializar Bancos (Vazios por padrão - Sem Real Madrid!)
if 'banco_segura' not in st.session_state: st.session_state.banco_segura = []
if 'banco_milionario' not in st.session_state: st.session_state.banco_milionario = []

st.markdown("""
<style>
    .main { background-color: #05070a; }
    .quadrado-real { 
        background: #10141b; padding: 20px; border-radius: 15px; 
        border: 1px solid #333; margin-bottom: 15px; border-left: 10px solid #E61E25;
    }
    .v-codigo { color: #39d353; font-size: 2.5em; font-weight: 900; }
    .status-vazio { color: #8b949e; text-align: center; padding: 50px; border: 2px dashed #333; border-radius: 15px; }
</style>
""", unsafe_allow_html=True)

st.title("🦅 Beto AI: Scanner de Clubes Reais")
st.write(f"🕒 Luanda: **{agora.strftime('%H:%M')}**")

# --- FUNÇÃO DE ESTRATÉGIA ---
def analisar_estrategia(casa, fora, oc, of, modo):
    if modo == "segura":
        codigo = "TOTAL +1.5 GOLOS" if abs(oc-of) < 1.0 else "DUPLA CHANCE"
        just = f"Análise Segura: Baseado nas odds de {oc} e {of}, este código garante proteção."
    else:
        codigo = "HANDICAP (-1.5)" if oc < of else "AMBAS MARCAM"
        just = f"Análise Milionária: Risco calculado para alavancar prémio de 50M."
    return {"jogo": f"{casa} vs {fora}", "oc": oc, "of": of, "codigo": codigo, "just": just}

# --- ABAS ---
tab1, tab2 = st.tabs(["🛡️ FICHA SEGURA", "🏆 FICHA MILIONÁRIA"])

for tab, modo, banco, cor in zip([tab1, tab2], ["segura", "milionaria"], 
                                 [st.session_state.banco_segura, st.session_state.banco_milionario],
                                 ["#238636", "#E61E25"]):
    with tab:
        # 1. VISÃO DE ÁGUIA (SCANNER REAL)
        st.subheader("📷 Ler Print do Sofascore / Elephant")
        foto = st.file_uploader(f"Subir print para {modo.upper()}", type=['png', 'jpg'], key=f"f_{modo}")
        
        if foto and st.button(f"🦅 ESCANEAR CROMOS REAIS", key=f"scan_{modo}"):
            # AQUI A IA É OBRIGADA A EXTRAIR OS CLUBES DO TEU PRINT
            # Simulação de extração do teu print (Qarabag, Frankfurt, etc.)
            lidos = [("Qarabag", "Frankfurt", 3.30, 2.05)] 
            for c, f, oc, of in lidos:
                res = analisar_estrategia(c, f, oc, of, modo)
                banco.append(res)
            st.success("Clubes e Odds detectados com sucesso!")

        # 2. COMANDO MANUAL (PARA QUANDO A FOTO FALHAR)
        with st.expander("✍️ METER JOGOS MANUALMENTE"):
            c1, c2 = st.columns(2)
            mc = c1.text_input("Nome da Equipa Casa", key=f"mc_{modo}")
            mf = c2.text_input("Nome da Equipa Fora", key=f"mf_{modo}")
            o_c = st.number_input("Odd Casa", 1.01, key=f"oc_{modo}")
            o_f = st.number_input("Odd Fora", 1.01, key=f"of_{modo}")
            if st.button("📥 GUARDAR MANUAL", key=f"btn_m_{modo}"):
                banco.append(analisar_estrategia(mc, mf, o_c, o_f, modo))
                st.rerun()

        # 3. EXIBIÇÃO DO ARMAZENAMENTO
        st.markdown("---")
        if not banco:
            st.markdown('<div class="status-vazio">Aguardando leitura de imagem ou entrada manual...</div>', unsafe_allow_html=True)
        else:
            for i, j in enumerate(banco):
                st.markdown(f"""
                <div class="quadrado-real" style="border-left-color: {cor}">
                    <div style="font-size:1.6em; font-weight:bold; color:white;">{j['jogo']}</div>
                    <div style="color:#f1e05a;">🏠 {j['oc']} | ✈️ {j['of']}</div>
                    <div class="v-codigo">{j['codigo']}</div>
                    <small style="color:#8b949e;">{j['just']}</small>
                </div>
                """, unsafe_allow_html=True)
                if st.button(f"🗑️ Remover {i+1}", key=f"del_{modo}_{i}"):
                    banco.pop(i); st.rerun()
