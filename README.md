# Projeto de Automação de Agentes com CrewAI, OpenAI e Llama

Este projeto tem como objetivo integrar e automatizar fluxos de trabalho de criação de conteúdo para redes sociais, análise de dados e automação de campanhas publicitárias, utilizando as APIs do **CrewAI**, **OpenAI** e **Llama**.

## Descrição Geral

O projeto permite o uso de agentes automatizados para gerenciar tarefas de conteúdo, análise de dados e automação de marketing. A eficácia do uso do **CrewAI** em comparação ao uso direto das APIs da **Llama** ou **OpenAI** depende do contexto e do tipo de tarefa que você está tentando realizar.

## Principais Componentes

1. **CrewAI**: Utilizado para fluxos de trabalho automatizados e agentes configuráveis que podem lidar com memória, histórico e delegação de tarefas.
2. **OpenAI**: API para processamento de linguagem natural (NLP), ideal para tarefas diretas de geração de textos.
3. **Llama**: Modelo de IA desenvolvido pela Meta, utilizado para tarefas de NLP semelhantes às da OpenAI.

## Comparação de Eficácia

- **CrewAI**: Indicado para tarefas complexas e que envolvem múltiplas interações, como a criação de calendários de conteúdo ou campanhas publicitárias detalhadas.
- **OpenAI e Llama**: Ideais para tarefas diretas e simples, como geração de textos com base em prompts curtos. O uso direto destas APIs pode ser mais rápido e eficiente quando a automação complexa não é necessária.

## Pré-requisitos

- **Docker** instalado no sistema.
- **Python 3.9+** instalado no ambiente de desenvolvimento.
- Uma conta na **OpenAI** com chave de API válida.
- O **CrewAI** instalado no projeto.

### Variáveis de Ambiente

Você deve criar um arquivo `.env` na raiz do projeto com as seguintes variáveis:

OPENAI_API_KEY=your-openai-api-key

Comando Docker para Rodar o Llama
Para rodar o modelo Llama localmente via Docker, execute o seguinte comando:

```bash
docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama
```

Esse comando irá iniciar o contêiner do Llama e expor a porta 11434 para acesso local.

Crie um ambiente virtual Python e ative-o:

```bash
python -m venv venv
source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
```

Instale as dependências do projeto:

```bash
pip install -r requirements.txt
```

Usando o CrewAI, OpenAI ou Llama
Para usar o Llama, defina "agent_choice": "llama".
Para usar o OpenAI, defina "agent_choice": "openai".
Para usar o CrewAI, defina "agent_choice": "crewai".
Exemplo de Arquivo JSON para Requisições
Aqui está um exemplo de requisição que pode ser feita à API:

json
Copy code
{
  "agent_choice": "crewai",
  "tasks": [
    {
      "agent_details": {
        "role": "Criador de Conteúdo",
        "goal": "Criar postagens para redes sociais",
        "backstory": "Especialista em conteúdo digital."
      },
      "description": "Escrever um post para LinkedIn sobre gestão de frotas."
    }
  ]
}
Como Rodar o Projeto
Inicie o servidor Flask:

bash
Copy code
python app.py
Faça uma requisição HTTP POST para o endpoint /execute-tasks, fornecendo um payload JSON no formato acima.

Comparação entre CrewAI, OpenAI e Llama
CrewAI
Automatização de Fluxos de Trabalho: Ideal para criar agentes que lidam com tarefas complexas, integrando memória e delegação de funções.
Configuração de Agentes: Cada agente pode ter papéis, objetivos e histórias configurados, úteis para fluxos de trabalho que exigem contexto contínuo.
OpenAI e Llama
Acesso Direto ao Modelo: Uso direto das APIs de IA com respostas rápidas para tarefas simples.
Menor Overhead: Melhor para uso em tarefas de geração de texto simples, sem a complexidade de gerenciar múltiplos agentes.
Custos
CrewAI: Pode adicionar uma camada de automação e gestão que implica custos adicionais, dependendo do serviço ou licenciamento.
OpenAI: Custo baseado no consumo de tokens. Exemplos:
GPT-3.5: A partir de $0,002 por 1.000 tokens.
GPT-4: Preços mais elevados.
Llama: Não tem API pública oficial, mas o acesso via plataformas de terceiros pode ter custos.
Quando Usar Cada Ferramenta?
CrewAI: Use quando precisa de automação avançada, múltiplos agentes e gestão de contexto/memória.
OpenAI ou Llama: Use para tarefas mais simples e diretas, como geração de respostas ou conteúdo curto.
Conclusão
Este projeto fornece uma estrutura para integrar a criação automatizada de conteúdo, campanhas publicitárias e análise de dados usando APIs poderosas de IA. Dependendo do seu caso de uso, você pode escolher entre o CrewAI, OpenAI ou Llama para maximizar a eficiência e eficácia.

Como Contribuir

Faça um fork deste repositório.

Crie uma nova branch:

git checkout -b feature/nova-feature
Faça as alterações e commit:

git commit -m 'Adiciona nova feature'
Envie suas alterações para o GitHub:

git push origin feature/nova-feature

Author: geraldoaax@gmail.com