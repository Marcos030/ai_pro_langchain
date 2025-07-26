# AI_GENERATED_CODE_START
# [AI Generated] Data: 19/03/2024
# Descrição: Exemplo básico com LangChain usando ChatGPT para gerar frases sobre a cor roxa
# Gerado por: Cursor AI
# Versão: LangChain 0.1.0, OpenAI 1.12.0

"""
Exemplo básico de uso do LangChain com OpenAI ChatGPT.
Este script demonstra como usar o LangChain para gerar frases criativas
baseadas na cor roxa.
"""

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage

def carregar_configuracoes():
    """
    Carrega as configurações de ambiente.
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
    """
    api_key = carregar_configuracoes()
    
    # Cria o modelo ChatOpenAI com configurações específicas
    llm = ChatOpenAI(
        api_key=api_key,
        model="gpt-4o-mini",  # Usando GPT-4o-mini conforme solicitado
        temperature=0.7,      # Criatividade moderada
        max_tokens=100        # Limita o tamanho da resposta
    )
    
    return llm

def gerar_frase_roxa(llm):
    """
    Gera uma frase criativa baseada na cor roxa.
    
    Args:
        llm: Modelo de linguagem configurado
        
    Returns:
        str: Frase gerada pelo modelo
    """
    # Prompt criativo para gerar frases sobre a cor roxa
    prompt = HumanMessage(content="""
    Gere uma frase curta e criativa (máximo 20 palavras) que capture a essência 
    e beleza da cor roxa. A frase deve ser filosófica e inspiradora, evocando 
    sentimentos positivos associados a esta cor majestosa.
    """)
    
    try:
        # Gera a resposta usando o modelo
        resposta = llm.invoke([prompt])
        return resposta.content.strip()
    except Exception as e:
        print(f"Erro ao gerar frase: {e}")
        return "Não foi possível gerar uma frase no momento."

def main():
    """
    Função principal que executa o exemplo.
    """
    print("=" * 60)
    print("🎨 EXEMPLO LANGCHAIN - GERADOR DE FRASES ROXAS 🎨")
    print("=" * 60)
    
    try:
        # Cria o modelo de linguagem
        print("🔧 Configurando modelo de linguagem...")
        llm = criar_modelo_llm()
        print("✅ Modelo configurado com sucesso!")
        
        print("\n🔄 Gerando frase criativa sobre a cor roxa...")
        
        # Gera a frase
        frase = gerar_frase_roxa(llm)
        
        print("\n" + "=" * 60)
        print("💜 FRASE GERADA:")
        print("=" * 60)
        print(f'"{frase}"')
        print("=" * 60)
        
        print("\n🎉 Exemplo executado com sucesso!")
        
    except Exception as e:
        print(f"\n❌ Erro durante a execução: {e}")
        print("Verifique se:")
        print("1. As dependências estão instaladas (pip install -r requirements.txt)")
        print("2. O arquivo config.env está presente com a chave da API")
        print("3. A chave da API é válida")

if __name__ == "__main__":
    main() 