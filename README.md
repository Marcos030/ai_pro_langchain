# AI_GENERATED_CODE_START
# [AI Generated] Data: 19/03/2024
# Descrição: Documentação do projeto de estudos LangChain
# Gerado por: Cursor AI
# Versão: LangChain 0.1.0

# Projeto de Estudos LangChain

Este projeto foi criado para estudar e experimentar com o framework LangChain, explorando suas funcionalidades e capacidades.

## Estrutura do Projeto

```
ai_pro_langchain/
├── requirements.txt      # Dependências do projeto
├── config.env           # Variáveis de ambiente
├── README.md           # Documentação
├── src/                # Código fonte
│   ├── __init__.py
│   ├── hello.py        # Exemplo básico com LangChain
│   └── utils/          # Utilitários
│       └── __init__.py
└── examples/           # Exemplos adicionais
    ├── __init__.py
    ├── firstAgent.py   # Exemplo de uso do agente Wikipedia + Math
    ├── fileUploader.py # Aplicação Streamlit para Q&A com documentos
    ├── headline_creator.py # Criador de títulos e roteiros para YouTube
    └── agents/         # Código dos agentes reutilizáveis
        ├── __init__.py
        └── wiki_math_agent.py # Agente Wikipedia + Math reutilizável
```

## Configuração

1. **Instalar dependências:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Configurar variáveis de ambiente:**
   - O arquivo `config.env` já contém a chave da OpenAI
   - Certifique-se de que o arquivo está no diretório raiz

3. **Executar os exemplos:**
   ```bash
   # Exemplo básico
   python src/hello.py
   
   # Exemplo do agente
   python examples/firstAgent.py
   
   # Aplicação Streamlit (Q&A com documentos)
   streamlit run examples/fileUploader.py
   
   # Criador de títulos para YouTube
   streamlit run examples/headline_creator.py
   ```

## Exemplos

### Hello World (hello.py)
Exemplo básico que utiliza o ChatGPT para gerar uma frase curta baseada na cor roxa.

### First Agent (examples/firstAgent.py)
Exemplo de uso do agente zero-shot com tools do Wikipedia e llm-math. Demonstra como usar agentes reutilizáveis para responder perguntas sobre inteligência artificial.

### File Uploader (examples/fileUploader.py)
Aplicação Streamlit completa para Q&A com documentos. Suporta upload de PDF, TXT, CSV, DOCX e imagens (JPEG/PNG) com OCR. Interface web interativa para análise inteligente de documentos. Utiliza automaticamente a chave da OpenAI do arquivo config.env.

### Headline Creator (examples/headline_creator.py)
Criador de títulos e roteiros para YouTube usando LangChain e pesquisa do Google via API Serper. Gera títulos SEO-friendly e roteiros completos baseados em pesquisas atuais. Interface Streamlit intuitiva para criadores de conteúdo.

## Tecnologias Utilizadas

- **Python 3.10+**
- **LangChain 0.1.0**
- **OpenAI API**
- **python-dotenv**

## Próximos Passos

Este projeto será expandido com mais exemplos e funcionalidades conforme o estudo do LangChain progride. 