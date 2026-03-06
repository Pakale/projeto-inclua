import streamlit as st
import pandas as pd

# Configuração da página (Front-End) ---
st.set_page_config(page_title="Projeto Inclua",
                   page_icon="🧩", layout="wide")

# Estilo simples para o título 
st.title("🧩 Projeto Inclua")
st.subheader("Ferramenta de Suporte ao Professor Inclusivo")

# --- Barra Lateral (Painel de Controle) ---
with st.sidebar:
    st.header("Configurações")
    nome_aluno = st.text_input("Nome do Aluno:", value="Ex: João da Silva")
    nivel = st.select_slider("Nível de Suporte (TEA):", options=[1, 2, 3])
    st.info(f"Visualizando recursos para Nível {nivel}")

# --- Corpo Principal (ABAS) ---
tab1, tab2, tab3 = st.tabs(["📚 Repositório", "✨ Adaptador (IA)", "🖊️ Relatórios"])

with tab1:
    st.header("Materiais do Governo Classificados")
    st.write("Estes materiais foram filtrados para o nível de suporte selecionado.")

    # Simulação de dados para o Front-end
    dados = {
        'Material': ['Guia de Alfabetização', 'Atividade Sensorial', 'Matemática Visual', 'Caderno de AEE'],
        'Nível': [1, 2, 3, 1]
    }
    df = pd.DataFrame(dados)
    st.dataframe(df)