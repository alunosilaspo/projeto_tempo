import os
import sqlite3
import pandas as pd
import streamlit as st

st.title("🌦️ Dashboard de Clima - Consulta")
st.write("Visualização dos dados meteorológicos salvos localmente no banco de dados.")

# Caminho para o banco de dados na pasta 'dados' na raiz do projeto
DB_PATH = os.path.join(os.path.dirname(__file__), '..', 'dados', 'weather.db')

if not os.path.exists(DB_PATH):
    st.warning("O banco de dados ainda não foi encontrado. Execute o script `coletor.py` primeiro!")
else:
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql("SELECT * FROM previsoes", conn)
    conn.close()

    if df.empty:
        st.info("O banco de dados está vazio.")
    else:
        cidades = df['cidade'].unique()
        cidade_selecionada = st.selectbox("Selecione a cidade:", cidades)

        df_filtrado = df[df['cidade'] == cidade_selecionada]

        st.subheader(f"Histórico de Previsões para: {cidade_selecionada}")
        st.dataframe(df_filtrado)

        if 'temp_max' in df_filtrado.columns:
            st.line_chart(df_filtrado.set_index('data')[['temp_max', 'temp_min']])