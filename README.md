# Análise de Dados

Este projeto cria uma aplicação web interativa para analisar dados de uma pesquisa. Utilizando Streamlit para a interface web e Plotly para a visualização de dados, a aplicação permite explorar os dados da pesquisa de forma dinâmica e visual.

## Funcionalidades

- Carregamento de dados de um arquivo CSV.
- Seleção e visualização de colunas específicas da pesquisa.
- Exibição de gráficos interativos (barras, pizza e linhas) para comparação de diferentes variáveis.

## Como Executar

1. Certifique-se de ter o Python instalado.
2. Instale as dependências necessárias:
    ```bash
    pip install streamlit pandas plotly
    ```
3. Execute a aplicação:
    ```bash
    streamlit run analise_dados.py
    ```
4. Acesse a aplicação em seu navegador pelo endereço fornecido pelo Streamlit.

## Estrutura do Código

- Carrega os dados do arquivo `dados.csv`.
- Permite a seleção de colunas para visualização.
- Exibe os dados em formato de tabela.
- Gera gráficos interativos (barras, pizza e linhas) para comparar diferentes variáveis com a variável "Coluna1".

## Requisitos

- Python 3.6+
- Streamlit
- Pandas
- Plotly
