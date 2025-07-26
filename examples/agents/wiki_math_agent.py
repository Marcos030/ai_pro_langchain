# AI_GENERATED_CODE_START
# [AI Generated] Data: 19/03/2024
# Descrição: Código de criação do agente Wikipedia + Math reutilizável
# Gerado por: Cursor AI
# Versão: LangChain 0.1.0, OpenAI 1.13.3+

"""
Módulo de criação do agente Wikipedia + Math.
Este módulo contém as funções para criar e configurar um agente zero-shot
que utiliza tools do Wikipedia e llm-math.
"""

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, AgentType, load_tools
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.tools import Tool

def carregar_configuracoes():
    """
    Carrega as configurações de ambiente.
    
    Returns:
        str: Chave da API OpenAI
    """
    # Carrega as variáveis de ambiente do arquivo config.env
    load_dotenv('config.env')
    
    # Verifica se a chave da API está configurada
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        raise ValueError("Chave da API OpenAI não encontrada. Verifique o arquivo config.env")
    
    return api_key

def criar_modelo_llm():
    """
    Cria e configura o modelo de linguagem usando OpenAI.
    
    Returns:
        ChatOpenAI: Modelo de linguagem configurado
    """
    api_key = carregar_configuracoes()
    
    # Cria o modelo ChatOpenAI com configurações específicas
    llm = ChatOpenAI(
        api_key=api_key,
        model="gpt-4o-mini",
        temperature=0.1,  # Baixa temperatura para respostas mais precisas
        max_tokens=1000   # Mais tokens para respostas detalhadas
    )
    
    return llm

def criar_tools(llm):
    """
    Cria as tools que o agente irá utilizar.
    
    Args:
        llm: Modelo de linguagem para a tool de matemática
        
    Returns:
        list: Lista de tools configuradas
    """
    # Tool do Wikipedia
    wikipedia_api = WikipediaAPIWrapper()
    wikipedia_tool = WikipediaQueryRun(api_wrapper=wikipedia_api)
    
    # Tool de matemática usando load_tools
    math_tools = load_tools(["llm-math"], llm=llm)
    
    # Configuração das tools com descrições claras
    tools = [
        Tool(
            name="Wikipedia",
            func=wikipedia_tool.run,
            description="Útil para buscar informações sobre tópicos, pessoas, lugares, eventos, etc. Use esta tool quando precisar de informações factuais ou históricas."
        )
    ]
    
    # Adiciona as tools de matemática
    tools.extend(math_tools)
    
    return tools

def criar_agente_wiki_math():
    """
    Cria o agente zero-shot com tools do Wikipedia e llm-math.
    
    Returns:
        AgentExecutor: Agente configurado
    """
    # Cria o modelo de linguagem
    llm = criar_modelo_llm()
    
    # Cria as tools
    tools = criar_tools(llm)
    
    # Cria o agente zero-shot com verbose=True
    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,  # Mostra o processo de pensamento do agente
        handle_parsing_errors=True,  # Trata erros de parsing
        max_iterations=5  # Limita o número de iterações para evitar loops infinitos
    )
    
    return agent 