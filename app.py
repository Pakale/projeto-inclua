import streamlit as st
import pandas as pd

# --- CONFIGURAÇÃO DA PÁGINA (FRONT-END) ---
st.set_page_config(page_title="Inclua - App de Acessibilidade", page_icon="🧩", layout="wide")

# Estilo simples para o título
st.title("🧩 Projeto Inclua")
st.subheader("Ferramenta de Suporte ao Professor Inclusivo")

# --- BARRA LATERAL (PAINEL DE CONTROLE) ---
with st.sidebar:
    st.header("Configurações")
    nome_aluno = st.text_input("Nome do Aluno:", value="Ex: J. S")
    nivel = st.select_slider("Nível de Suporte (TEA):", options=[1, 2, 3])
    st.info(f"Visualizando recursos para Nível {nivel}")

# --- CORPO PRINCIPAL (ABAS) ---
tab1, tab2, tab3 = st.tabs(["📚 Repositório", "✨ Adaptador (IA)", "📝 Relatórios"])

with tab1:
    st.header("Materiais do Governo Classificados")
    st.write("Estes materiais foram filtrados para o nível de suporte selecionado.")
    
    # Simulação de dados para o Front-end
    dados = {
        'Material': ['Guia de Alfabetização', 'Atividade Sensorial', 'Matemática Visual', 'Caderno de AEE'],
        'Nível': [1, 3, 2, 1],
        'Link': ['Acessar PDF', 'Acessar PDF', 'Acessar PDF', 'Acessar PDF']
    }
    df = pd.DataFrame(dados)
    
    # Filtro automático
    filtro = df[df['Nível'] == nivel]
    st.table(filtro)

with tab2:
    st.header("Simulador de Adaptação")
    st.write("Como a IA ainda não está ligada, aqui você vê como será o visual:")
    
    texto_exemplo = st.text_area("Cole o texto da aula aqui:", height=150)
    
    if st.button("Testar Visual da Adaptação"):
        st.success("O Front-end está funcionando! Quando a IA estiver ativa, o texto adaptado aparecerá abaixo.")
        st.info(f"Aqui apareceria a versão simplificada para o aluno {nome_aluno}.")

with tab3:
    st.header("Diário de Bordo")
    st.write("Espaço para o professor anotar a evolução do dia.")
    st.text_input("O que aconteceu hoje?")
    st.button("Salvar Registro")

# Rodapé
st.divider()
st.caption("Protótipo do Projeto Integrador - Nome do APP.")
