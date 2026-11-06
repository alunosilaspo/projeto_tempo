import os
import json
import sqlite3
import requests
from dotenv import load_dotenv

# Como o .env está na raiz e este script está em 'app/', subimos um nível (..)
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '.env'))
API_KEY = os.getenv("VISUAL_CROSSING_API_KEY")

LOCATION = "Juiz de Fora"
UNIT_GROUP = "metric"

# Define o caminho para a pasta 'dados' na raiz do projeto
PASTA_DESTINO = os.path.join(os.path.dirname(__file__), '..', 'dados')
os.makedirs(PASTA_DESTINO, exist_ok=True)

DB_PATH = os.path.join(PASTA_DESTINO, "weather.db")

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS previsoes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cidade TEXT,
            data TEXT,
            temp_max REAL,
            temp_min REAL,
            umidade REAL,
            condicoes TEXT
        )
    ''')
    conn.commit()
    conn.close()

def salvar_no_banco(cidade, data_json):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    dias = data_json.get('days', [])
    
    for dia in dias:
        cursor.execute('''
            INSERT INTO previsoes (cidade, data, temp_max, temp_min, umidade, condicoes)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (
            cidade,
            dia.get('datetime'),
            dia.get('tempmax'),
            dia.get('tempmin'),
            dia.get('humidity'),
            dia.get('conditions')
        ))
        
    conn.commit()
    conn.close()

def executar_coleta():
    if not API_KEY:
        print("Erro: A chave da API (VISUAL_CROSSING_API_KEY) não foi encontrada no arquivo .env!")
        return

    url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{LOCATION}?unitGroup={UNIT_GROUP}&key={API_KEY}&contentType=json"
    
    print(f"Buscando dados meteorológicos para {LOCATION}...")
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        cidade_limpa = LOCATION.lower().replace(" ", "_")
        filename_json = os.path.join(PASTA_DESTINO, f"weather_{cidade_limpa}.json")
        
        with open(filename_json, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"[{LOCATION}] JSON bruto salvo em: {filename_json}")
        
        init_db()
        salvar_no_banco(LOCATION, data)
        print(f"[{LOCATION}] Dados gravados com sucesso no banco SQLite!")

    except requests.exceptions.HTTPError as http_err:
        print(f"Erro HTTP ao buscar dados: {http_err}")
    except Exception as err:
        print(f"Ocorreu um erro inesperado: {err}")

if __name__ == "__main__":
    executar_coleta()