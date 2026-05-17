import streamlit as st
import pandas as pd
import plotly.express as px

# =========================
# CONFIGURAÇÃO DA PÁGINA
# =========================
st.set_page_config(
    page_title="EcoLife Carbon App",
    page_icon="🌍",
    layout="wide"
)

# =========================
# ESTILO VISUAL
# =========================
st.markdown("""
<style>
.main {
    background-color: #f5f7fa;
}

h1, h2, h3 {
    color: #0E6655;
}

.stButton>button {
    background-color: #117864;
    color: white;
    border-radius: 10px;
    height: 3em;
    width: 100%;
    font-size: 18px;
}

.stMetric {
    background-color: white;
    padding: 10px;
    border-radius: 12px;
    box-shadow: 0px 0px 8px rgba(0,0,0,0.1);
}
</style>
""", unsafe_allow_html=True)

# =========================
# SIDEBAR
# =========================
st.sidebar.title("🌱 EcoLife App")
st.sidebar.info("""
Aplicativo educativo para cálculo de impacto ambiental pessoal.
""")

st.sidebar.success("Objetivo: reduzir emissões 🌎")

# =========================
# TÍTULO
# =========================
st.title("🌍 Calculadora Ambiental Inteligente")
st.markdown("Calcule sua pegada de carbono mensal e descubra como melhorar seu impacto ambiental.")

# =========================
# TRANSPORTE
# =========================
st.header("🚗 Transporte")

col1, col2 = st.columns(2)

with col1:
    km_carro = st.number_input(
        "Km de Carro/Moto por mês",
        min_value=0.0,
        step=50.0
    )

with col2:
    km_transporte_pub = st.number_input(
        "Km Transporte Público",
        min_value=0.0,
        step=50.0
    )

# =========================
# CASA
# =========================
st.header("🏠 Consumo Residencial")

col3, col4 = st.columns(2)

with col3:
    kwh_energia = st.number_input(
        "Energia elétrica (kWh)",
        min_value=0.0,
        step=20.0
    )

with col4:
    m3_agua = st.number_input(
        "Água consumida (m³)",
        min_value=0.0,
        step=2.0
    )

# =========================
# LIXO
# =========================
st.header("🗑️ Resíduos")

lixo_diario_kg = st.slider(
    "Quantidade de lixo diário (kg)",
    0.0,
    20.0,
    1.0
)

percentual_reciclado = st.slider(
    "Percentual reciclado (%)",
    0,
    100,
    20
)

# =========================
# DIETA
# =========================
st.header("🥗 Dieta")

dieta = st.selectbox(
    "Selecione seu perfil alimentar:",
    [
        "Forte consumidor de carne",
        "Consumidor moderado",
        "Vegetariano",
        "Vegano"
    ]
)

# =========================
# OBRAS
# =========================
st.header("🏗️ Obras")

fez_obra = st.radio(
    "Fez reforma nos últimos 12 meses?",
    ("Não", "Sim")
)

escopo_obra = "Nenhum"

if fez_obra == "Sim":
    escopo_obra = st.selectbox(
        "Tipo da obra",
        [
            "Pequena",
            "Média",
            "Grande"
        ]
    )

# =========================
# FATORES
# =========================
FATOR_CARRO = 0.18
FATOR_ONIBUS = 0.05
FATOR_ENERGIA = 0.09
FATOR_AGUA = 0.35
FATOR_LIXO = 0.5

fator_dieta = 250

if "moderado" in dieta.lower():
    fator_dieta = 140
elif "vegetariano" in dieta.lower():
    fator_dieta = 90
elif "vegano" in dieta.lower():
    fator_dieta = 60

fator_obra = 0

if fez_obra == "Sim":
    if escopo_obra == "Pequena":
        fator_obra = 1500 / 12
    elif escopo_obra == "Média":
        fator_obra = 5000 / 12
    else:
        fator_obra = 12000 / 12

# =========================
# BOTÃO
# =========================
if st.button("🌍 Calcular Pegada"):

    emissao_transporte = (
        km_carro * FATOR_CARRO +
        km_transporte_pub * FATOR_ONIBUS
    )

    emissao_casa = (
        kwh_energia * FATOR_ENERGIA +
        m3_agua * FATOR_AGUA
    )

    lixo_total = lixo_diario_kg * 30

    lixo_nao_reciclado = lixo_total * (
        1 - percentual_reciclado / 100
    )

    emissao_lixo = lixo_nao_reciclado * FATOR_LIXO

    total = (
        emissao_transporte +
        emissao_casa +
        emissao_lixo +
        fator_dieta +
        fator_obra
    )

    st.divider()

    st.subheader("📊 Resultado Final")

    c1, c2, c3 = st.columns(3)

    c1.metric("🚗 Transporte", f"{emissao_transporte:.1f} kg")
    c2.metric("🏠 Casa", f"{emissao_casa:.1f} kg")
    c3.metric("🗑️ Resíduos", f"{emissao_lixo:.1f} kg")

    st.metric("🌍 Pegada Total", f"{total:.2f} kgCO₂e/mês")

    # =========================
    # BARRA DE IMPACTO
    # =========================
    progresso = min(total / 1000, 1.0)

    st.progress(progresso)

    # =========================
    # AVALIAÇÃO
    # =========================
    if total <= 280:
        st.success("🟢 Pegada Ambiental Boa")

    elif total <= 550:
        st.warning("🟡 Pegada Moderada")

    else:
        st.error("🔴 Pegada Alta")

    # =========================
    # EQUIVALÊNCIA AMBIENTAL
    # =========================
    arvores = total / 22

    st.info(
        f"🌳 Seriam necessárias aproximadamente "
        f"{arvores:.1f} árvores por mês "
        f"para compensar suas emissões."
    )

    # =========================
    # GRÁFICO
    # =========================
    dados = pd.DataFrame({
        "Categoria": [
            "Transporte",
            "Casa",
            "Lixo",
            "Dieta",
            "Obras"
        ],
        "Emissões": [
            emissao_transporte,
            emissao_casa,
            emissao_lixo,
            fator_dieta,
            fator_obra
        ]
    })

    fig = px.pie(
        dados,
        names="Categoria",
        values="Emissões",
        title="Distribuição das Emissões"
    )

    st.plotly_chart(fig, use_container_width=True)

    # =========================
    # DICAS PERSONALIZADAS
    # =========================
    st.subheader("💡 Recomendações Inteligentes")

    if km_carro > 500:
        st.write("🚴 Considere usar bicicleta ou transporte coletivo.")

    if percentual_reciclado < 30:
        st.write("♻️ Aumente sua taxa de reciclagem.")

    if "carne" in dieta.lower():
        st.write("🥗 Reduzir carne vermelha ajuda muito o planeta.")

    if kwh_energia > 300:
        st.write("💡 Desligue aparelhos em standby e use LED.")