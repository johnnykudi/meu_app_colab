import streamlit as st
import pandas as pd
import plotly.express as px
import random
from datetime import datetime

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title='Kudi Finance', layout='wide')

# --- ESTILO CUSTOMIZADO ---
st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    .stButton>button { background-color: #2ECC71; color: white; border-radius: 10px; }
    .kudi-card { background-color: #f8f9fa; padding: 20px; border-radius: 15px; border-left: 5px solid #2ECC71; margin-bottom: 10px; }
    h1, h2, h3 { color: #1B1F23; }
    </style>
    """, unsafe_allow_html=True)

# --- SIMULAÇÃO DE DADOS ---
def get_financial_tips(perfil, gastos_hoje):
    tips = {
        "Jovem": [
            "Evite gastar muito com saldo de dados, use o Wi-Fi sempre que possível.",
            "Kudi Tip: Já pensou em poupar 500 Kz por semana para o seu primeiro negócio?",
            "Cuidado com as saídas constantes à Ilha, o orçamento pode apertar!"
        ],
        "Empreendedor": [
            "Separe o dinheiro do negócio do seu dinheiro pessoal!",
            "Dica Kudi: Reinvista 20% do lucro de hoje em stock.",
            "Registe cada venda no Zungue ou na banca, o controlo é a alma do negócio."
        ]
    }

    if gastos_hoje > 5000:
        return f"⚠️ Alerta Kudi: Gastaste {gastos_hoje} Kz hoje. Tenta reduzir nos próximos 2 dias."
    return random.choice(tips[perfil])

# --- SIDEBAR ---
st.sidebar.title("Kudi Finance")
menu = st.sidebar.selectbox("Menu", ["Dashboard", "Metas"])
perfil = st.sidebar.radio("Perfil", ["Jovem", "Empreendedor"])

if menu == "Dashboard":
    st.title("Olá, Angolano! 👋")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<div class="kudi-card"><h3>Saldo Atual</h3><h2>150.000 Kz</h2></div>', unsafe_allow_html=True)
    
    df_gastos = pd.DataFrame({
        'Categoria': ['Alimentação', 'Transporte', 'Renda', 'Lazer', 'Negócio'],
        'Valor': [15000, 8000, 10000, 5000, 7000]
    })

    fig = px.pie(df_gastos, values='Valor', names='Categoria',
                 title='Onde estás a gastar o teu Kwanza?',
                 color_discrete_sequence=['#2ECC71', '#27AE60', '#1B1F23', '#BDC3C7', '#222222'])
    # Corrigido: use_container_width=True para width='stretch'
    st.plotly_chart(fig, width='stretch')
  import streamlit as st
import pandas as pd
import plotly.express as px
import random

# Aplicando a mesma correção de parâmetros para evitar avisos de depreciação
st.set_page_config(page_title='Kudi Finance', layout='wide')

# Exemplo de gráfico corrigido
df_gastos = pd.DataFrame({
    'Categoria': ['Alimentação', 'Transporte', 'Renda', 'Lazer', 'Negócio'],
    'Valor': [15000, 8000, 10000, 5000, 7000]
})

fig = px.pie(df_gastos, values='Valor', names='Categoria', 
             title='Distribuição de Gastos (Kz)')

# Atualizado para o novo padrão do Streamlit
st.plotly_chart(fig, width='stretch')
app_code = r"""import streamlit as st
import pandas as pd
import plotly.express as px
import random
from datetime import datetime

st.set_page_config(page_title='Kudi Finance', layout='wide')
st.markdown('<style>.main { background-color: #ffffff; } .stButton>button { background-color: #2ECC71; color: white; border-radius: 10px; } .kudi-card { background-color: #f8f9fa; padding: 20px; border-radius: 15px; border-left: 5px solid #2ECC71; margin-bottom: 10px; } h1, h2, h3 { color: #1B1F23; }</style>', unsafe_allow_html=True)

def get_financial_tips(perfil, gastos_hoje):
    tips = {'Jovem': ['Evite gastar muito com saldo de dados.', 'Poupe 500 Kz/semana.'], 'Empreendedor': ['Separe o dinheiro pessoal do negócio.', 'Reinvista 20% do lucro.']}
    if gastos_hoje > 5000: return f'⚠️ Alerta: Gastaste {gastos_hoje} Kz hoje! Cuidado com o orçamento.'
    return random.choice(tips[perfil])

st.sidebar.title('Kudi Finance')
menu = st.sidebar.selectbox('Menu', ['Dashboard', 'Metas'])
perfil = st.sidebar.radio('Perfil', ['Jovem', 'Empreendedor'])

if menu == 'Dashboard':
    st.title('Olá, Angolano! 👋')
    st.markdown("<div style='background-color:#e0f7e0; padding:10px; border-radius:10px'><h3>Saldo Atual: 50.000 Kz</h3></div>", unsafe_allow_html=True)
    st.subheader('Registar Gasto')
    col_a, col_b = st.columns(2)
    with col_a:
        gasto = st.number_input('Quanto gastou hoje (Kz)?', min_value=0)
    with col_b:
        categoria = st.selectbox('Categoria:', ['Alimentação','Transporte','Lazer','Negócios'])
    if gasto > 10000:
        st.warning('Cuidado! Gastou muito hoje em relação à sua média.')
    elif gasto > 0:
        st.warning(get_financial_tips(perfil, gasto))
    else:
        st.info(f'Dica: {get_financial_tips(perfil, 0)}')
    df = pd.DataFrame({
        'Categoria': ['Alimentação','Transporte','Lazer','Negócios'],
        'Gastos': [12000, 5000, 2000, 8000]
    })
    fig = px.pie(df, names='Categoria', values='Gastos', title='Gastos Mensais',
                 color_discrete_sequence=['#2ECC71', '#27AE60', '#1B1F23', '#BDC3C7'])
    st.plotly_chart(fig, use_container_width=True)
"""

with open('app.py', 'w') as f:
    f.write(app_code)
