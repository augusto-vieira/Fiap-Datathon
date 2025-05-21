## 📜 Índice

- [📜 Índice](#-índice)
- [🏁​ Introdução](#-introdução)
- [📋 Preparação do Ambiente](#-preparação-do-ambiente)
- [🐳 Executando com Docker](#-executando-com-docker)
- [🤖 RecrutAi Crew](#-recrutai-crew)
- [💻 Instalação](#-instalação)
- [🏹 Uso](#-uso)
- [🛠️ Customização](#️-customização)
- [🧠 Entendendo o Crew](#-entendendo-o-crew)
- [🆘 Suporte](#-suporte)
- [🥁 Melhorias](#-melhorias)
- [🪪 Autores](#-autores)

## 🏁​ Introdução
Neste desafio, os estudantes colocam em prática seus conhecimentos em Machine Learning para resolver problemas reais de uma empresa. O foco é aplicar Inteligência Artificial no processo de recrutamento e seleção, utilizando dados da Decision, empresa especializada em conectar talentos ao setor de tecnologia da informação.

A missão é desenvolver uma solução baseada em IA que otimize entrevistas, identifique perfis ideais e melhore o match entre candidatos e vagas. Para isso, é necessário apresentar uma proposta completa, inteligente e funcional, capaz de transformar o processo seletivo por meio da tecnologia.

Nossa proposta para o desafio foi utilizar agentes de IA como facilitadores do recrutamento. Esses sistemas autônomos atuam como especialistas na área, com uma função clara: analisar a descrição da vaga, considerar os dados dos candidatos e interpretar os comentários feitos pelos recrutadores. A partir dessas informações, os agentes realizam uma triagem precisa, destacando os candidatos que realmente atendem aos requisitos técnicos da posição.

Assim, os agentes de IA tornam o processo seletivo mais ágil, consistente e objetivo, oferecendo suporte valioso aos recrutadores na tomada de decisão.

![RecrutAI](https://github.com/augusto-vieira/Fiap-Datathon/img/1.png) C:\PROJECTS\Fiap-Datathon\img\1.png
![Analise_1](https://github.com/augusto-vieira/Fiap-Datathon/img/2.png) C:\PROJECTS\Fiap-Datathon\img\2.png
![Analise_2](https://github.com/augusto-vieira/Fiap-Datathon/img/3.png) 

| ![Imagem 1](1.png) | ![Imagem 2](2.png) |
|:------------------------:|:------------------------:|
| Analise              | Sugestão              |


## 📋 Preparação do Ambiente
Antes de rodar o projeto, é necessário adicionar manualmente os arquivos de dados, pois eles não estão disponíveis no repositório.

1. 🐑 Clone este repositório:

    ```bash
    git clone https://github.com/augusto-vieira/Fiap-Datathon.git
    ```

2. 📁 Entre no diretório do projeto:

    ```bash
    cd Fiap-Datathon
    ```
3. 📁 Dentro da pasta data, adicione os seguintes arquivos:
    ```bash
    ├── data
    │   ├── applicants
    │   │   ├── applicants.json
    │   ├── prospects
    │   │   ├── prospects.json
    │   └── vagas
    │       ├── vagas.json       
    ```

## 🐳 Executando com Docker

Você também pode rodar a aplicação usando Docker:

1. 📂 Acesse a pasta raiz da aplicação (Fiap-Datathon).

2. ▶️ Execute o comando:

    ```bash
    docker compose up -d
    ```
4. 🦙 Instale o modelo llama3.2 (ou outro modelo de sua preferência):
    ```bash
    docker exec -it ollama ollama pull llama3.2
    ```
5. 🔎 Para verificar **quais modelos estão disponíveis no Ollama** dentro do seu contêiner:
    ```bash
    docker exec -it ollama ollama list
    ```
   🔎 Verificar o modelo que está sendo **utilizado** no seu ambiente:
    ```bash
   docker exec -it api_agent_ai printenv MODEL
    ```
1. 🌐 A aplicação estará disponível em:  
    [http://localhost:8501/](http://localhost:8501/)

2. 🛑 Para parar a aplicação, use:
    ```bash
    docker-compose down
    ``` 

## 🤖 RecrutAi Crew

Bem-vindo ao projeto **RecrutAi Crew**, desenvolvido com o poder do [crewAI](https://crewai.com)!  
Este projeto cria um sistema multiagente de IA de forma fácil e eficiente, aproveitando toda a flexibilidade do framework **crewAI**. Nosso objetivo é permitir que agentes colaborem em tarefas complexas, maximizando inteligência e resultados.


## 💻 Instalação

Certifique-se de ter o **Python >=3.10 e <3.13** instalado.  
Este projeto utiliza o [UV](https://docs.astral.sh/uv/) para gerenciamento de dependências.

1. 📦 Instale o `uv`:

    ```bash
    pip install uv
    ```

2. 📁 Acesse a pasta raiz do projeto.

3. 🔒 (Opcional) Trave e instale as dependências:

    ```bash
    crewai install
    ```

4. 🔑 Adicione sua chave `OPENAI_API_KEY` no arquivo `.env`.

## 🏹 Uso

Para iniciar sua equipe de agentes de IA e começar a execução das tarefas:

```bash
crewai run
```

Este comando inicializa o **RecrutAi Crew**, montando os agentes e distribuindo as tarefas conforme definido.  
Ao executar o exemplo padrão, será criado um arquivo `report.md` com o resultado de uma pesquisa sobre LLMs.

## 🛠️ Customização

Você pode personalizar seu projeto facilmente:

- ✍️ Edite `src/recrut_ai/config/agents.yaml` para definir seus agentes.
- ✍️Edite `src/recrut_ai/config/tasks.yaml` para definir suas tarefas.
- ✍️Edite `src/recrut_ai/crew.py` para adicionar lógica personalizada, ferramentas e argumentos.
- ✍️Edite `src/recrut_ai/main.py` para adicionar entradas customizadas para agentes e tarefas.

## 🧠 Entendendo o Crew

O **RecrutAi Crew** é composto por múltiplos agentes de IA, cada um com seus papéis, objetivos e ferramentas.

- 🚩As tarefas estão definidas em `config/tasks.yaml`.
- 🚩As configurações dos agentes estão em `config/agents.yaml`.

Esses agentes colaboram entre si para realizar objetivos mais complexos. 🚀

## 🆘 Suporte

Se precisar de ajuda ou quiser saber mais:

- 📚 [Documentação oficial do crewAI](https://docs.crewai.com)
- 🐙 [Repositório no GitHub](https://github.com/joaomdmoura/crewai)
- 💬 [Comunidade no Discord](https://discord.com/invite/X4JWnZnxPb)
- 🤖 [Chat com as documentações](https://chatg.pt/DWjSBZn)

Vamos criar maravilhas juntos com a força e simplicidade do **crewAI**! ✨

## 🥁 Melhorias
- Upload de currículos para análise.
- Integração com LinkedIn API para buscar candidatos.

---
## 🪪 Autores

- [Augusto Vieira - RM357293](www.linkedin.com/in/whoami-augusto-vieira)
- [João Kienen    - RM357561](https://www.linkedin.com/in/jkienen/?jobid=1234)
- [Lucas Galhardo - RM357287](https://www.linkedin.com/in/lucas-galhardo/?jobid=1234)
- [Rafael Ribeiro - RM357611](https://github.com/raffaell95)
