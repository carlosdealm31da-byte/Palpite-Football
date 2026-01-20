import streamlit as st
import random
from datetime import datetime, time
import pytz
import re

# Configuração de Luanda
angola_tz = pytz.timezone('Africa/Luanda')
agora = datetime.now(angola_tz)

st.set_page_config(page_title="Beto AI - O General Supremo", layout="wide")

# Inicializar Bancos de Dados
if 'banco_manual' not in st.session_state: st.session_state.banco_manual = []
if 'banco_segura' not in st.session_state: st.session_state.banco_segura = []
if 'banco_milionario' not in st.session_state: st.session_state.banco_milionario = []

# Estilo Elite
st.markdown("""
<style>
    .main { background-color: #0b0e11; }
    .card-ia { background-color: #1a1d23; padding: 20px; border-radius: 12px; border: 1px solid #333; margin-bottom: 15px; }
    .alerta-ia { background-color: #701c1c; padding: 15px; border-radius: 8px; border-left: 5px solid #ff4b4b; margin: 10px 0; color: white; }
    .v-codigo { color: #39d353; font-size: 2.2em; font-weight: bold; }
    .resumo-topo { background: #0d1117; padding: 20px; border-radius: 15px; border: 2px solid #238636; text-align: center; margin-bottom: 20px; }
</style>
""", unsafe_allow_html=True)

st.title("🎯 Beto AI: Inteligência Crítica e Decisória")
st.write(f"🕒 Luanda: **{agora.strftime('%H:%M')}**")

# --- MOTOR DE INTELIGÊNCIA CRÍTICA ---
def analisar_critica_ia(casa, fora, oc, of, modo):
    confianca = random.uniform(70.0, 99.0)
    
    # Se for manual, a IA age como consultora crítica
    if modo == "manual":
        if abs(oc - of) < 0.2:
            veredito = "⚠️ AVISO: Jogo extremamente equilibrado. Inserir este jogo manualmente é arriscado."
            sugestao = "AMBAS MARCAM (CÓDIGO RECOMENDADO)"
            motivo = "Identifiquei que não há um favorito claro. O motivo de escolher Ambas é a utilidade estatística de ataques parelhos."
        else:
            veredito = "✅ JOGO ANALISADO: Boa escolha tática."
            sugestao = "VENCEDOR DIRETO" if oc < of else "VENCEDOR DIRETO (FORA)"
            motivo = f"A odd de {oc} mostra que o {casa} tem domínio. Aceito a tua escolha manual com este código."
    
    # Se for Segura ou Milionária, a IA DECIDE SOZINHA
    else:
        if modo == "milionaria":
            sugestao = "HANDICAP (-1.5)" if oc < 1.7 else "AMBAS & +2.5"
            veredito = "🚀 DECISÃO MILIONÁRIA: Selecionado pelo App."
            motivo = "A minha inteligência decidiu que este jogo é o motor para os 50M. Não aceito margens menores."
        else:
            sugestao = "DUPLA CHANCE"
            veredito = "🛡️ DECISÃO SEGURA: Selecionado pelo App."
            motivo = "Para a ficha segura, a minha vontade é proteger o capital. Este é o único código aceitável."
            
    return {"veredito": veredito, "codigo": sugestao, "motivo": motivo, "confianca": f"{confianca:.1f}%"}

# --- FUNÇÃO DE ARMAZENAMENTO ---
def salvar_no_banco(lista, jogo, codigo, odd, hora):
    if len(lista) < 40:
        lista.append({"confronto": jogo, "codigo": codigo, "odd": odd, "hora": hora})
        return True
    return False

# --- ABAS ---
tab1, tab2, tab3 = st.tabs(["✍️ COMANDO MANUAL", "🛡️ FICHA SEGURA", "🏆 FICHA MILIONÁRIA"])

with tab1:
    st.subheader("⚙️ Tu indicas o jogo, a IA critica e gera o código")
    with st.container():
        c1, c2, c3 = st.columns([2,2,1])
        ca = c1.text_input("Equipa Casa", key="ca_m")
        fo = c2.text_input("Equipa Fora", key="fo_m")
        ho = c3.text_input("Hora", "20:00", key="ho_m")
        o1 = st.number_input("Odd Casa", 1.01, key="o1_m")
        o2 = st.number_input("Odd Fora", 1.01, key="o2_m")

        if ca and fo:
            analise = analisar_critica_ia(ca, fo, o1, o2, "manual")
            st.markdown(f"""
            <div class="alerta-ia">
                <b>{analise['veredito']}</b><br>
                <small>{analise['motivo']}</small>
            </div>
            <div class="card-ia">
                <span style="color:#8b949e;">CÓDIGO GERADO PELA IA:</span><br>
                <span class="v-codigo">{analise['codigo']}</span>
            </div>
            """, unsafe_allow_html=True)
            
            if st.button("📥 CONFIRMAR E GUARDAR NO BANCO MANUAL"):
                salvar_no_banco(st.session_state.banco_manual, f"{ca} vs {fo}", analise['codigo'], o1, ho)
                st.rerun()

with tab3:
    st.subheader("🏆 Vontade do Aplicativo (Meta 50M)")
    dados = st.text_area("Cole os dados do print/texto aqui")
    if st.button("🦅 DEIXAR IA DECIDIR E GUARDAR TUDO"):
        jogos = re.findall(r'(\w+)\s+vs\s+(\w+)\s+([\d.]+)\s+([\d.]+)\s+(\d{2}:\d{2})', dados)
        for j in jogos:
            res = analisar_critica_ia(j[0], j[1], float(j[2]), float(j[3]), "milionaria")
            salvar_no_banco(st.session_state.banco_milionario, f"{j[0]} vs {j[1]}", res['codigo'], float(j[2])*1.8, j[4])
        st.success("A IA escolheu os jogos e guardou no banco milionário!")

    # Exibição do acumulado
    odd_m = 1.0
    for j in st.session_state.banco_milionario: odd_m *= j['odd']
    st.markdown(f"<div class='resumo-topo'><h1>💰 {(200*odd_m):,.2f} KZ</h1><small>{len(st.session_state.banco_milionario)}/40 Jogos</small></div>", unsafe_allow_html=True)

    for j in st.session_state.banco_milionario:
        st.markdown(f"<div class='card-ia'><b>{j['confronto']}</b><br><span class='v-codigo'>{j['codigo']}</span></div>", unsafe_allow_html=True)

if st.sidebar.button("🗑️ LIMPAR TUDO"):
    st.session_state.banco_manual = []
    st.session_state.banco_milionario = []
    st.rerun()
