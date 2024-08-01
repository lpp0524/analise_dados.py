import streamlit as st
import pandas as pd
import plotly.express as px

#streamlit run analise_dados.py

st.set_page_config(layout="wide")

file_path = "caminho/para/seu/arquivo/dados.csv"
try:
    df = pd.read_csv(file_path, encoding="latin-1", sep=",")
except FileNotFoundError:
    st.error("Arquivo 'dados.csv' não encontrado. Certifique-se de que o caminho do arquivo está correto.")

string_columns = ['Coluna1', 'Coluna2', 'Coluna3', 'Coluna4', 'Coluna5']
df[string_columns] = df[string_columns].astype(str)

colunas_ordenadas = [
    'Coluna1',
    'Coluna2',
    'Coluna3',
    'Coluna4',
    'Coluna5'
]

original_df = df.copy()

df = df[colunas_ordenadas]

st.title("Análise de Dados")

if not df.empty:
    st.subheader("Configurações das Colunas")
    selected_columns = st.multiselect("Selecione as colunas na ordem desejada", df.columns)
    if selected_columns:
        df = df[selected_columns]

    st.subheader("Visualização dos Dados")
    st.dataframe(df, height=300, width=800)

st.subheader("Opções de Exibição de Gráficos")

for column in original_df.columns:
    if column != 'Coluna1':
        tipo_grafico = st.selectbox(f"Tipo de gráfico para comparar {column} por Coluna1:", [
            "Gráficos em Barra",
            "Gráficos em Pizza",
            "Gráficos em Linhas"
        ])

        if tipo_grafico == "Gráficos em Barra":
            count_data = original_df.groupby(['Coluna1', column]).size().reset_index(name='Count')
            bar_fig = px.bar(count_data, x='Coluna1', y='Count', color=column,
                            title=f"Comparação de {column} por Coluna1")
            st.plotly_chart(bar_fig, use_container_width=True)

        elif tipo_grafico == "Gráficos em Pizza":
            pie_data = original_df.groupby([column, 'Coluna1']).size().reset_index(name='Count')
            pie_fig = px.pie(pie_data, names=column, values='Count',
                            title=f"Comparação de {column} por Coluna1")
            st.plotly_chart(pie_fig, use_container_width=True)

        elif tipo_grafico == "Gráficos em Linhas":
            line_data = original_df.groupby(['Coluna1', column]).size().reset_index(name='Count')
            line_fig = px.line(line_data, x='Coluna1', y='Count', color=column,
                            title=f"Comparação de {column} por Coluna1")
            st.plotly_chart(line_fig, use_container_width=True)
