# 🌦️ Projeto Previsão do Tempo (Weather Pipeline & Dashboard)

> Um pipeline de dados meteorológicos desenvolvido em Python para consumo da API da Visual Crossing, armazenamento estruturado de arquivos JSON, persistência em Banco de Dados Relacional (SQLite) e visualização interativa através de um Dashboard em Streamlit.

---

## 📂 Estrutura do Projeto

O repositório está organizado da seguinte forma:

```text
projeto_tempo/
│
├── app/
│   ├── app.py          # Dashboard interativo (Streamlit)
│   └── coletor.py      # Script de Backend/ETL para coleta e salvamento dos dados
│
├── dados/
│   ├── weather.db      # Banco de dados SQLite contendo o histórico consolidado
│   └── weather_*.json  # Arquivos JSON brutos salvos por localidade
│
├── notebooks/
│   └── script_api.ipynb# Notebook exploratório inicial
│
├── .env                # Variáveis de ambiente (Chave da API - Ignorado pelo Git)
├── .gitignore          # Arquivos e pastas ignorados pelo controle de versão
└── README.md           # Documentação do projeto


🚀 Tecnologias Utilizadas
Python 3.x

Requests (Consumo da API REST)

Streamlit (Interface gráfica e dashboard web)

SQLite & Pandas (Manipulação e persistência de dados relacionais)

Python-dotenv (Gerenciamento seguro de variáveis de ambiente)

⚙️ Como Configurar e Executar o Projeto
1. Pré-requisitos
Certifique-se de ter o Python instalado na sua máquina. Em seguida, clone o repositório e instale as dependências necessárias:

Bash
pip install requests pandas streamlit python-dotenv
2. Configurando a Chave da API (.env)
Crie um arquivo chamado .env na raiz do projeto (projeto_tempo/) e insira a sua chave da Visual Crossing Weather:

Snippet de código
VISUAL_CROSSING_API_KEY=sua_chave_aqui_12345
3. Executando o Coletor (Backend / ETL)
Para buscar os dados mais recentes na API, atualizar o arquivo JSON bruto e popular o banco de dados weather.db, execute a partir da raiz do projeto:

Bash
python app/coletor.py
4. Executando o Dashboard (Streamlit)
Para abrir a interface de consulta e visualização dos dados meteorológicos no seu navegador, execute:

Bash
python -m streamlit run app/app.py
📊 Funcionalidades
Coleta Automatizada: Requisição estruturada via script para consulta de dados meteorológicos por localidade.

Armazenamento Híbrido: Salvamento de logs e dados brutos em formato .json e consolidação relacional em banco de dados SQLite.

Dashboard Interativo: Visualização de tabelas e gráficos dinâmicos de temperatura máxima, mínima e umidade utilizando o Streamlit.

✒️ Autor
Desenvolvido por Silas Oliveira.