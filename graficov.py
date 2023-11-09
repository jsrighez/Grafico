from dash import Dash, html, dcc, Input, Output
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import your_database_library  # Importe a biblioteca de acesso ao banco de dados/MUDAR

graphic = dash.Dash(__name__)

# Conecte-se ao seu banco de dados
df = your_database_library.connect_to_database()
#MUDAR
fig = px.pie(df, names='Você costuma ler?', title='Leitura por Gênero (Homens)') #arrumar

title_style = {
    'font-family': 'Nunito',  # Defina a fonte desejada aqui
    'font-size': '40px',  # Tamanho da fonte
    'font-weight': 'bold', # Peso da fonte (opcional)
    'color': '#28B465'
    }

graphic.layout = html.Div(children=[
    children=[
    html.Link(
    rel='stylesheet',
    href='https://fonts.googleapis.com/css2?family=Nunito:wght@300&display=swap',
    ),
    html.H1(children='Máquina de Gráficos |||', style=title_style),
    
    dcc.Graph(
        id='graph',
        figure=fig
    )
])
graphic.layout = html.Div([
    dcc.Graph(id='graph'),
])

@graphic.callback(
    Output('graph', 'figure'),
    [Input('your-input-component', 'value')]  # Se você tiver um componente de entrada - mudar
)
def update_graph(selected_value):
    # Use o valor selecionado para fazer uma consulta ao banco de dados
    query = f"SELECT * FROM sua_tabela WHERE coluna = {selected_value}"
    data = your_database_library.execute_query(df, query)
    result = your_database_library.execute_query(df, query)

    if result:
        title = result[0]['title_column']  # Assumindo que a coluna do título é chamada 'title_column'
    else:
        title = "Gráfico de PIzza"  # Defina um título padrão se não houver resultados no banco de dados

    # Agora, use os dados do banco de dados para atualizar o gráfico
    # Aqui, você pode criar um gráfico com base nos dados do banco de dados

    figure = {
        'data': [...],  # Seus dados do gráfico
        'layout': {
            'title': title,  # Defina o título com base nos dados do banco de dados
        }
    }

    config = {
        # Configurações adicionais do gráfico, se necessário
    }

    return figure, config

if __name__ == '__main__':
    graphic.run_server(debug=True)