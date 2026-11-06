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