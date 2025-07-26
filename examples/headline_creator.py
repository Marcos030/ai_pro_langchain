# AI_GENERATED_CODE_START
# [AI Generated] Data: 19/03/2024
# Descrição: Criador de títulos e roteiros para YouTube usando LangChain e Serper
# Gerado por: Cursor AI
# Versão: LangChain 0.1.0, OpenAI 1.13.3+

"""
Criador de Títulos e Roteiros para YouTube.
Este script utiliza LangChain para gerar títulos e roteiros de vídeos
baseados em pesquisas do Google via API Serper.
"""

import os
import requests
import streamlit as st
from dotenv import load_dotenv
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from langchain.memory import ConversationBufferMemory

# Carregar variáveis de ambiente
load_dotenv('config.env')

# Configurar chaves de API
openai_api_key = os.getenv('OPENAI_API_KEY')
serper_api_key = os.getenv('SERPER_API_KEY')

if not openai_api_key:
    st.error("OpenAI API Key não encontrada no arquivo config.env")
    st.stop()

if not serper_api_key:
    st.error("Serper API Key não encontrada no arquivo config.env")
    st.stop()

# Debug: Verificar se as chaves estão sendo carregadas (apenas para desenvolvimento)
if st.checkbox("🔧 Modo Debug (mostrar informações das chaves)"):
    st.write(f"OpenAI Key (primeiros 10 chars): {openai_api_key[:10]}...")
    st.write(f"Serper Key (primeiros 10 chars): {serper_api_key[:10]}...")

# Configurar a chave de API da OpenAI no ambiente
os.environ['OPENAI_API_KEY'] = openai_api_key

# Definindo uma classe para pesquisar no Google usando a API Serper.dev
class SerperAPIWrapper:
    def __init__(self, api_key):
        self.api_key = api_key
        self.url = "https://google.serper.dev/search"

    def run(self, query):
        """
        Executa uma pesquisa no Google via API Serper.
        
        Args:
            query (str): Consulta de pesquisa
            
        Returns:
            str: Snippets dos resultados da pesquisa
        """
        headers = {
            "X-API-KEY": self.api_key,
            "Content-Type": "application/json"
        }
        payload = {
            "q": query
        }
        
        try:
            response = requests.post(self.url, headers=headers, json=payload)
            if response.status_code == 200:
                results = response.json()
                snippets = [item['snippet'] for item in results.get('organic', [])]
                return "\n".join(snippets)
            elif response.status_code == 403:
                return f"Erro 403 - Chave da API inválida ou sem permissão. Verifique se a chave Serper está correta."
            elif response.status_code == 401:
                return f"Erro 401 - Não autorizado. Verifique se a chave Serper está correta."
            else:
                return f"Erro na pesquisa: {response.status_code} - {response.text}"
        except Exception as e:
            return f"Erro na requisição: {str(e)}"

# Configurando o título da aplicação no Streamlit
st.title('🦜🔗 YouTube GPT Creator')
st.markdown("Crie títulos e roteiros para vídeos do YouTube com IA")

# Campo de entrada para o usuário escrever o tema
prompt = st.text_input('Escreva aqui o tema do conteúdo', 
                      placeholder="Ex: inteligência artificial, receitas de bolo, dicas de programação...")

# Definindo templates de prompt para o título do vídeo e o roteiro
title_template = PromptTemplate(
    input_variables=['topic'], 
    template='Escreva um título atrativo e SEO-friendly para um vídeo do YouTube sobre: {topic}. O título deve ser curto, impactante e gerar curiosidade.'
)

script_template = PromptTemplate(
    input_variables=['title', 'google_research'], 
    template='Escreva um roteiro completo de vídeo do YouTube baseado neste título: {title}. Use as informações desta pesquisa do Google para enriquecer o conteúdo: {google_research}. O roteiro deve incluir introdução, desenvolvimento e conclusão.'
)

# Configurando memória para armazenar o histórico de conversação
title_memory = ConversationBufferMemory(input_key='topic', memory_key='chat_history')
script_memory = ConversationBufferMemory(input_key='title', memory_key='chat_history')

# Inicializando o modelo de linguagem
llm = OpenAI(temperature=0.9, model="gpt-3.5-turbo-instruct")

# Configurando as cadeias de LLM
title_chain = LLMChain(
    llm=llm, 
    prompt=title_template, 
    verbose=True, 
    output_key='title', 
    memory=title_memory
)

script_chain = LLMChain(
    llm=llm, 
    prompt=script_template, 
    verbose=True, 
    output_key='script', 
    memory=script_memory
)

# Inicializando o wrapper da API Serper.dev
google_search = SerperAPIWrapper(api_key=serper_api_key)

# Botão para testar a API Serper
if st.button("🧪 Testar API Serper"):
    with st.spinner("Testando conexão com Serper..."):
        test_result = google_search.run("teste")
        st.write("Resultado do teste:", test_result)

# Mostrando os resultados na tela se houver um prompt
if prompt:
    with st.spinner("Gerando título e roteiro..."):
        try:
            # Gerar o título do vídeo
            title = title_chain.run(prompt)
            
            # Realizar a pesquisa no Google
            google_research = google_search.run(prompt)
            
            # Gerar o roteiro do vídeo
            script = script_chain.run(title=title, google_research=google_research)

            # Exibir resultados
            st.success("✅ Conteúdo gerado com sucesso!")
            
            st.markdown("### 🎬 Título do Vídeo")
            st.write(title)
            
            st.markdown("### 📝 Roteiro do Vídeo")
            st.write(script)

            # Expansores para mostrar histórico e pesquisa
            with st.expander('📚 Histórico de Títulos'):
                st.info(title_memory.buffer)

            with st.expander('📚 Histórico de Roteiros'):
                st.info(script_memory.buffer)

            with st.expander('🔍 Pesquisa do Google'):
                st.info(google_research)
                
        except Exception as e:
            st.error(f"Erro ao gerar conteúdo: {str(e)}")
            st.error("Verifique se as chaves de API estão corretas e se há conexão com a internet.")
