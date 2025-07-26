# AI_GENERATED_CODE_START
# [AI Generated] Data: 19/03/2024
# Descrição: Exemplo de uso do agente Wikipedia + Math
# Gerado por: Cursor AI
# Versão: LangChain 0.1.0, OpenAI 1.13.3+

"""
Exemplo de uso do agente Wikipedia + Math.
Este exemplo demonstra como usar o agente zero-shot com tools do Wikipedia
e llm-math para responder perguntas sobre inteligência artificial.
"""

import sys
import os

# Adiciona o diretório agents ao path para importar o módulo
sys.path.append(os.path.join(os.path.dirname(__file__), 'agents'))

from agents.wiki_math_agent import criar_agente_wiki_math

def executar_agente(agent):
    """
    Executa o agente com uma pergunta sobre IA.
    
    Args:
        agent: Agente configurado
    """
    # Pergunta sobre inteligência artificial
    #pergunta = "Conte-me sobre inteligência artificial. Quais são os principais marcos históricos e como ela evoluiu ao longo do tempo?"
    pergunta = "quanto é 8*8?"

    
    print("=" * 80)
    print("🤖 AGENTE ZERO-SHOT - CONSULTA SOBRE INTELIGÊNCIA ARTIFICIAL 🤖")
    print("=" * 80)
    print(f"❓ Pergunta: {pergunta}")
    print("=" * 80)
    print("\n🔄 Executando agente...\n")
    
    try:
        # Executa o agente
        resposta = agent.invoke({"input": pergunta})
        
        print("\n" + "=" * 80)
        print("✅ RESPOSTA DO AGENTE:")
        print("=" * 80)
        print(resposta["output"])
        print("=" * 80)
        
    except Exception as e:
        print(f"\n❌ Erro durante a execução do agente: {e}")
        print("Verifique se:")
        print("1. As dependências estão instaladas")
        print("2. A conexão com a internet está funcionando")
        print("3. A chave da API é válida")

def main():
    """
    Função principal que executa o exemplo do agente.
    """
    try:
        # Cria o agente usando o módulo reutilizável
        print("🔧 Criando agente zero-shot com Wikipedia e LLM Math...")
        agent = criar_agente_wiki_math()
        print("✅ Agente criado com sucesso!")
        
        # Executa o agente
        executar_agente(agent)
        
        print("\n🎉 Exemplo do agente executado com sucesso!")
        print("\n💡 Dica: Você pode modificar a pergunta no código para testar diferentes consultas!")
        
    except Exception as e:
        print(f"\n❌ Erro durante a configuração: {e}")
        print("Verifique se:")
        print("1. As dependências estão instaladas (pip install -r requirements.txt)")
        print("2. O arquivo config.env está presente com a chave da API")
        print("3. A chave da API é válida")

if __name__ == "__main__":
    main() 