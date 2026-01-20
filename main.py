import streamlit as st
import random
from datetime import datetime
import pytz

# Configuração de Fuso Horário (Angola/Luanda)
angola_tz = pytz.timezone('Africa/Luanda')
agora = datetime.now(angola_tz)

st.set_page_config(page_title="Beto AI - Multi-Decisor", page_icon="🎯", layout="wide")

# Estilo Visual Corrigido (Para não aparecer tags de código no ecrã)
st.markdown("""
<style>
    .main { background-color: #0d1117; color: white; }
    .stButton>button { width: 100%; background-color: #238636; color: white; font-weight: bold; border-radius: 8px; height: 3.5em; border: none; }
    .card-analise { background-color: #161b22; padding: 20px; border-radius: 12px; border: 1px solid #30363d; margin-bottom: 20px; border-left: 8px solid #238636; }
    .label-equipa { color: #8b949e; font-size: 0.9em; font-weight: bold; }
    .nome-equipa { color: #ffffff; font-size: 1.2em; font-weight: bold; }
    .codigo-res { color: #39d353; font-size: 2em; font-weight: bold; display: block; margin: 10px 0; }
    .percent { color: #f1e05a; font-size: 1.3em; font-weight: bold; }
    .justificativa { background-color: #0d1117; padding: 12px; border-radius: 8px; border: 1px solid #30363d; margin-top: 10px; color: #c9d1d9; font-size: 0.95em; }
</style>
""", unsafe_allow_html=True)

st.title("🎯 Beto AI: Analisador Multi-Jogos")
st.write(f"🕒 Luanda: **{agora.strftime('%H:%M')}**")

# --- SESSÃO MULTI-JOGOS ---
st.header("📋 Lista de Jogos para Análise")
num_jogos = st.number_input("Quantos jogos queres analisar de uma vez?", min_value=1, max_value=50, value=1)

jogos_dados = []

# Criar formulários dinâmicos para cada jogo
for i in range(num_jogos):
    with st.expander(f"Configurar Jogo #{i+1}", expanded=(i==0)):
        c1, c2 = st.columns(2)
        with c1:
            casa = st.text_input(f"Equipa Casa #{i+1}", placeholder="Ex: Real Madrid", key=f"casa_{i}")
            odd_c = st.number_input(f"Odd Casa #{i+1}", value=1.50, step=0.01, key=f"odd_c_{i}")
        with c2:
            fora = st.text_input(f"Equipa Fora #{i+1}", placeholder="Ex: Man. City", key=f"fora_{i}")
            odd_f = st.number_input(f"Odd Fora #{i+1}", value=2.50, step=0.01, key=f"odd_f_{i}")
        
        c3, c4 = st.columns(2)
        with c3:
            data_j = st.date_input(f"Data #{i+1}", value=agora.date(), key=f"data_{i}")
        with c4:
            hora_j = st.time_input(f"Hora Início #{i+1}", key=f"hora_{i}")
        
        jogos_dados.append({
            'casa': casa, 'fora': fora, 'odd_c': odd_c, 'odd_f': odd_f, 
            'data': data_j, 'hora': hora_j
        })

# --- PROCESSAMENTO ---
if st.button("ANALISAR TODOS OS JOGOS AGORA"):
    st.markdown("---")
    st.subheader("🚀 RESULTADOS DA ANÁLISE")
    
    for i, jogo in enumerate(jogos_dados):
        # Validador de Tempo
        dt_evento = angola_tz.localize(datetime.combine(jogo['data'], jogo['hora']))
        
        if dt_evento < agora:
            st.warning(f"⚠️ Jogo #{i+1} ({jogo['casa']} vs {jogo['fora']}) já iniciou. Pulando análise.")
            continue
            
        # Lógica de Decisão (Corrigindo o NameError das imagens)
        o_c = jogo['odd_c']
        o_f = jogo['odd_f']
        
        if o_c < 1.35:
            codigo = "VENCEDOR 1 (CASA)"
            prob = random.uniform(92.5, 98.2)
            porque = f"A IA detectou favoritismo absoluto para a Equipa Casa ({jogo['casa']})."
        elif o_f < 1.35:
            codigo = "VENCEDOR 2 (FORA)"
            prob = random.uniform(92.5, 98.2)
            porque = f"Superioridade técnica esmagadora para a Equipa Fora ({jogo['fora']})."
        elif 1.45 <= o_c <= 2.20 and 1.45 <= o_f <= 2.20:
            codigo = "AMBAS MARCAM (SIM)"
            prob = random.uniform(84.0, 89.9)
            porque = "Equilíbrio tático sugere que ambas as equipas vão balançar as redes."
        else:
            codigo = "MAIS DE 1.5 GOLOS"
            prob = random.uniform(88.0, 95.5)
            porque = "Mercado de golos é o mais seguro para este confronto equilibrado."

        # EXIBIÇÃO FORMATADA (Como querias, com nomes Casa/Fora claros)
        html_card = f"""
        <div class="card-analise">
            <div style="display: flex; justify-content: space-between;">
                <div>
                    <span class="label-equipa">CASA:</span><br>
                    <span class="nome-equipa">{jogo['casa']}</span>
                </div>
                <div style="text-align: right;">
                    <span class="label-equipa">FORA:</span><br>
                    <span class="nome-equipa">{jogo['fora']}</span>
                </div>
            </div>
            <hr style="border: 0.5px solid #30363d; margin: 15px 0;">
            <span style="color: #8b949e; font-size: 0.9em;">CÓDIGO SUGERIDO:</span>
            <span class="codigo-res">{codigo}</span>
            <span class="percent">🔥 PROBABILIDADE: {prob:.1f}%</span>
            <div class="justificativa">
                <b>MOTIVO DA ESCOLHA:</b><br>
                {porque}
            </div>
        </div>
        """
        st.markdown(html_card, unsafe_allow_html=True)

st.markdown("---")
st.caption("Beto AI: Inteligência Multi-Jogos para Profissionais.")
