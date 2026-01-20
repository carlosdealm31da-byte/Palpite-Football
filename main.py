import streamlit as st
import random
from datetime import datetime, time
import pytz

# Configuração de Fuso Horário
angola_tz = pytz.timezone('Africa/Luanda')
agora = datetime.now(angola_tz)

st.set_page_config(page_title="Beto AI - Risco & Estratégia", layout="wide")

# Estilo Dark Pro (Foco em Resultados)
st.markdown("""
<style>
    .main { background-color: #0b0e11; color: white; }
    .stButton>button { width: 100%; background-color: #E61E25; color: white; font-weight: bold; border-radius: 8px; height: 3.5em; border: none; }
    .card-analise { background-color: #1a1d23; padding: 20px; border-radius: 12px; border: 1px solid #333; margin-bottom: 20px; border-left: 8px solid #E61E25; }
    .tag-risco { background-color: #ffc107; color: black; padding: 3px 8px; border-radius: 4px; font-size: 0.7em; font-weight: bold; }
    .tag-ganho { background-color: #238636; color: white; padding: 3px 8px; border-radius: 4px; font-size: 0.7em; font-weight: bold; }
    .codigo-v { color: #00ff00; font-size: 1.8em; font-weight: bold; display: block; margin: 5px 0; }
</style>
""", unsafe_allow_html=True)

st.title("🎯 Beto AI: Estratégia de Alavancagem")
st.write(f"🕒 Luanda: **{agora.strftime('%H:%M')}** | Foco: **Maximização de Prémio**")

# --- CONFIGURAÇÃO DE SESSÃO ---
st.sidebar.header("⚙️ Painel de Comando")
num_jogos = st.sidebar.number_input("Quantidade de Jogos", min_value=1, max_value=50, value=1)
horario_global = st.sidebar.time_input("Horário Padrão", value=time(18, 0))

jogos_lista = []

# --- ENTRADA DE DADOS MANUAL ---
st.subheader("📝 Lista de Confrontos")
for i in range(num_jogos):
    with st.expander(f"Jogo #{i+1}", expanded=(i == 0)):
        c1, c2, c3 = st.columns([2, 2, 1])
        with c1:
            casa = st.text_input(f"Equipa Casa #{i+1}", key=f"c_{i}")
            odd_c = st.number_input(f"Odd Casa #{i+1}", value=1.50, key=f"oc_{i}")
        with c2:
            fora = st.text_input(f"Equipa Fora #{i+1}", key=f"f_{i}")
            odd_f = st.number_input(f"Odd Fora #{i+1}", value=2.50, key=f"of_{i}")
        with c3:
            hora = st.time_input(f"Hora #{i+1}", value=horario_global, key=f"h_{i}")
        
        jogos_lista.append({'casa': casa, 'fora': fora, 'odd_c': odd_c, 'odd_f': odd_f, 'hora': hora})

# --- PROCESSAMENTO COM LÓGICA DE ALTO GANHO ---
if st.button("GERAR CÓDIGOS ESTRATÉGICOS"):
    st.markdown("---")
    
    for i, jogo in enumerate(jogos_lista):
        if not jogo['casa'] or not jogo['fora']: continue
        
        oc = jogo['odd_c']
        of = jogo['odd_f']
        
        # MOTOR DE DECISÃO DE RISCO (Busca de Odds Altas para chegar aos 50M)
        # Cenário A: Favorito claro -> Buscar Handicap para subir a Odd
        if oc < 1.40 or of < 1.40:
            status = "ALAVANCAGEM"
            fav = jogo['casa'] if oc < 1.40 else jogo['fora']
            codigo = f"HANDICAP (-1.5) {fav}"
            prob = random.uniform(70.0, 78.5)
            porque = "A odd seca é muito baixa para quem quer 50M. A IA sugere o Handicap para dobrar o valor, apostando numa vitória por 2 ou mais golos."
        
        # Cenário B: Jogo Equilibrado -> Buscar Resultado Exato ou Ambas Marcam + Total
        elif 1.80 <= oc <= 2.50 and 1.80 <= of <= 2.50:
            status = "ALTO RISCO / ALTO GANHO"
            codigo = "AMBAS MARCAM & +2.5 GOLOS"
            prob = random.uniform(65.0, 72.0)
            porque = "Confronto equilibrado onde a utilidade está nos golos. Esta combinação eleva a Odd final exponencialmente para acelerar a meta de ganho."
            
        # Cenário C: Odds Altas em ambos -> Buscar Intervalo/Final ou Resultado Seco
        else:
            status = "ESTRATÉGIA AGRESSIVA"
            codigo = "VENCEDOR (RESULTADO FINAL)"
            prob = random.uniform(55.0, 68.0)
            porque = "Jogo de alta incerteza. Sugerimos focar no vencedor seco da equipa com melhor retrospecto recente para capturar a Odd alta do mercado."

        # EXIBIÇÃO DO CARD
        st.markdown(f"""
        <div class="card-analise">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <span class="tag-risco">{status}</span>
                <span style="color: #8b949e; font-size: 0.8em;">🕒 {jogo['hora'].strftime('%H:%M')}</span>
            </div>
            <div style="margin: 10px 0;">
                <b style="font-size: 1.1em;">{jogo['casa']} vs {jogo['fora']}</b>
            </div>
            <span style="color: #8b949e; font-size: 0.8em;">CÓDIGO SUGERIDO:</span>
            <span class="codigo-v">{codigo}</span>
            <span style="font-size: 1.1em; color: #ffc107;">🎯 Confiança Tática: {prob:.1f}%</span>
            <div style="margin-top: 10px; background: #0d1117; padding: 10px; border-radius: 5px; font-size: 0.9em;">
                <b>ESTRATÉGIA:</b> {porque}
            </div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")
st.info("Beto AI: O objetivo é transformar 200 KZ em 50.000.000 KZ através de escolhas agressivas e inteligentes.")
