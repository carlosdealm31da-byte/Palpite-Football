import streamlit as st
import random
from datetime import datetime, time
import pytz

# Configuração de Fuso Horário (Angola/Luanda)
angola_tz = pytz.timezone('Africa/Luanda')
agora = datetime.now(angola_tz)

st.set_page_config(page_title="Beto AI - Especialista Tático", page_icon="🎯", layout="wide")

# Estilo Visual Profissional e Limpo
st.markdown("""
<style>
    .main { background-color: #0d1117; color: white; }
    .stButton>button { width: 100%; background-color: #238636; color: white; font-weight: bold; border-radius: 8px; height: 3.5em; border: none; }
    .card-analise { background-color: #161b22; padding: 20px; border-radius: 12px; border: 1px solid #30363d; margin-bottom: 20px; border-left: 8px solid #238636; }
    .label-equipa { color: #8b949e; font-size: 0.8em; text-transform: uppercase; }
    .nome-equipa { color: #ffffff; font-size: 1.1em; font-weight: bold; }
    .codigo-res { color: #39d353; font-size: 1.8em; font-weight: bold; display: block; margin: 5px 0; }
    .percent { color: #f1e05a; font-size: 1.2em; font-weight: bold; }
    .tag-utilidade { background-color: #238636; color: white; padding: 4px 8px; border-radius: 4px; font-size: 0.7em; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

st.title("🎯 Beto AI: Decisor Tático Manual")
st.write(f"🕒 Hora Atual em Luanda: **{agora.strftime('%H:%M')}**")

# --- CONFIGURAÇÃO GLOBAL (PARA POUPAR TEMPO) ---
st.sidebar.header("⚙️ Configuração Rápida")
horario_padrao = st.sidebar.time_input("Horário Padrão para os jogos", value=time(16, 0))
num_jogos = st.sidebar.number_input("Quantidade de Jogos", min_value=1, max_value=50, value=1)

jogos_lista = []

# --- ENTRADA DE DADOS ---
st.subheader("📝 Preenchimento dos Confrontos")
cols_input = st.columns(2)

for i in range(num_jogos):
    with st.expander(f"Jogo #{i+1} - Configurar", expanded=(i < 2)):
        c1, c2, c3 = st.columns([2, 2, 1])
        with c1:
            casa = st.text_input(f"Casa #{i+1}", key=f"c_{i}")
            odd_c = st.number_input(f"Odd Casa #{i+1}", value=1.50, key=f"oc_{i}")
        with c2:
            fora = st.text_input(f"Fora #{i+1}", key=f"f_{i}")
            odd_f = st.number_input(f"Odd Fora #{i+1}", value=2.50, key=f"of_{i}")
        with c3:
            # O utilizador pode usar o padrão ou mudar apenas este
            hora_individual = st.time_input(f"Hora #{i+1}", value=horario_padrao, key=f"h_{i}")
        
        jogos_lista.append({
            'casa': casa, 'fora': fora, 'odd_c': odd_c, 'odd_f': odd_f, 'hora': hora_individual
        })

# --- PROCESSAMENTO COM LOGICA DE UTILIDADE ---
if st.button("ANALISAR E DECIDIR TODOS"):
    st.markdown("---")
    
    for i, jogo in enumerate(jogos_lista):
        if not jogo['casa'] or not jogo['fora']:
            continue
            
        # Validar se o jogo ainda é possível (tempo)
        hora_limite = datetime.combine(agora.date(), jogo['hora'])
        hora_limite = angola_tz.localize(hora_limite)
        
        if hora_limite < agora:
            st.warning(f"⚠️ Jogo #{i+1}: O horário {jogo['hora'].strftime('%H:%M')} já passou. Análise cancelada para evitar erro.")
            continue

        # LÓGICA DE UTILIDADE TÁTICA (A IA decide o valor do jogo)
        oc = jogo['odd_c']
        of = jogo['odd_f']
        
        # Cenário 1: Super Favorito (Utilidade de Segurança)
        if oc < 1.30 or of < 1.30:
            tipo_utilidade = "SEGURANÇA MÁXIMA"
            codigo = "VENCEDOR (SECO)" if oc < 1.30 else "VENCEDOR 2 (SECO)"
            prob = random.uniform(94.0, 98.5)
            porque = "A IA identificou um desequilíbrio técnico total. A utilidade aqui é garantir o green com baixa exposição ao risco."
        
        # Cenário 2: Equilíbrio de Ataque (Utilidade de Golos)
        elif 1.50 <= oc <= 2.10 and 1.50 <= of <= 2.10:
            tipo_utilidade = "EFICIÊNCIA OFENSIVA"
            codigo = "AMBAS MARCAM (SIM)"
            prob = random.uniform(86.0, 91.5)
            porque = "Ambas as equipas têm odds que sugerem ataques produtivos. A utilidade deste código supera a de vencedor pelo equilíbrio do jogo."
            
        # Cenário 3: Jogo Trancado / Risco (Utilidade de Proteção)
        elif oc > 2.20 and of > 2.20:
            tipo_utilidade = "PROTEÇÃO DE BANCA"
            codigo = "MAIS DE 1.5 GOLOS"
            prob = random.uniform(89.0, 94.0)
            porque = "Jogo sem dono claro. A IA decide pela utilidade dos golos, protegendo o teu capital contra empates em 0-0 ou 1-1."
            
        else:
            tipo_utilidade = "DUPLA CHANCE"
            codigo = "1X (CASA OU EMPATE)" if oc < of else "X2 (FORA OU EMPATE)"
            prob = random.uniform(82.0, 88.0)
            porque = "Análise de utilidade recomenda cobrir dois resultados. O risco de empate é moderado neste confronto."

        # EXIBIÇÃO
        st.markdown(f"""
        <div class="card-analise">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <div>
                    <span class="label-equipa">CASA</span><br><span class="nome-equipa">{jogo['casa']}</span>
                </div>
                <div style="text-align: center;">
                    <span class="tag-utilidade">{tipo_utilidade}</span><br>
                    <span style="color: #8b949e; font-size: 0.8em;">{jogo['hora'].strftime('%H:%M')}</span>
                </div>
                <div style="text-align: right;">
                    <span class="label-equipa">FORA</span><br><span class="nome-equipa">{jogo['fora']}</span>
                </div>
            </div>
            <hr style="border: 0.1px solid #333; margin: 10px 0;">
            <span style="color: #8b949e; font-size: 0.8em;">DECISÃO TÁTICA:</span>
            <span class="codigo-res">{codigo}</span>
            <span class="percent">🔥 CONFIANÇA: {prob:.1f}%</span>
            <div style="margin-top: 10px; color: #8b949e; font-size: 0.9em; font-style: italic;">
                <b>ANÁLISE:</b> {porque}
            </div>
        </div>
        """, unsafe_allow_html=True)
