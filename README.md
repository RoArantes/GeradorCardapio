Projeto Gerador de Cardápio com IA 🍳🤖

Este é um projeto de demonstração que utiliza a API Google Gemini para sugerir receitas e cardápios com base em uma lista de ingredientes fornecida pelo usuário.
O projeto cumpre os requisitos de [criação de um produto com integração à API Gemini ], sendo dividido em duas partes principais:

Backend (API): Um servidor em Python usando FastAPI que recebe requisições, processa o prompt e se comunica com a API do Google Gemini.
Frontend (Interface Web): Uma página estática em HTML, CSS e JavaScript  que permite ao usuário final interagir com o sistema.

⚙️ Tecnologias Utilizadas
Backend:
Python 3.9+ 
FastAPI (Framework web) 
Uvicorn (Servidor ASGI) 
google-generativeai (Biblioteca oficial do Gemini) 
python-dotenv (Gerenciador de variáveis de ambiente) 

Frontend:
HTML5
CSS3 (para estilização básica)
JavaScript (para lógica e requisições fetch)

📦 Instalação e Configuração
Siga os passos abaixo para configurar e executar o projeto em sua máquina local.

1. Pré-requisitos
Python: Certifique-se de ter o Python 3.9 ou superior instalado.
Chave de API do Gemini: Você precisa de uma chave de API válida do Google AI Studio.

2. Configuração do Ambiente
Crie a pasta do projeto e abra-a no seu editor de código (ex: VS Code).
Crie um Ambiente Virtual para isolar as dependências:

Bash
python -m venv .venv
Ative o Ambiente Virtual:

No Windows:
PowerShell
.\.venv\Scripts\activate
No macOS/Linux:

Bash
source .venv/bin/activate

3. Instalação das Dependências
Crie um arquivo chamado requirements.txt na raiz do projeto com o seguinte conteúdo :
fastapi
uvicorn
google-generativeai
python-dotenv

Instale os pacotes listados:
Bash
pip install -r requirements.txt

4. Configuração da Chave de API
Crie um arquivo chamado .env na raiz do projeto.
Adicione sua chave de API do Google Gemini a este arquivo :
GOOGLE_API_KEY=sua_chave_aqui

▶️ Como Rodar o Programa
O projeto precisa que o Backend (API) e o Frontend (página web) sejam executados separadamente.

1. Executando o Backend (API)
O backend é responsável por se conectar ao Gemini.

Certifique-se de que seu ambiente virtual (.venv) está ativo.
Execute o servidor Uvicorn no seu terminal:
Bash
uvicorn main:app --reload --port 8001
Usamos a porta 8001 para evitar conflitos com a porta 8000.

O --reload faz o servidor reiniciar automaticamente se você alterar o main.py.

O terminal deve exibir: Uvicorn running on http://127.0.0.1:8001. Deixe este terminal rodando.

2. Executando o Frontend (Interface Web)
O frontend é um arquivo HTML simples.
Encontre o arquivo index.html na pasta do seu projeto.
Abra o index.html diretamente no seu navegador (ex: clicando duas vezes sobre ele).

🍽️ Como Usar
Com o backend rodando no terminal e o index.html aberto no navegador:
Digite os ingredientes que você tem disponíveis na caixa de texto. (Ex: "ovos, farinha, leite").
Clique no botão "Gerar Cardápio".
Aguarde alguns segundos. A área "Sugestão da IA" será atualizada com uma receita ou sugestão enviada pelo Gemini.
