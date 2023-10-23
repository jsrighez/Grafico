import pandas as pd
from dash import Dash, html, dcc, Input, Output
import plotly.express as px

# Suponha que você tenha um DataFrame com os dados, como o seguinte:
df = pd.read_excel("Respostas form.xlsx") 

app = Dash(__name__)

app.layout = html.Div([
    html.H1(children='Gráfico de Leitura por Gênero (Homens)'),
    dcc.Graph(id='grafico_leitura_genero_homens')
])

@app.callback(
    Output('grafico_leitura_genero_homens', 'figure'),
)
def atualizar_grafico():
    # Filtra os dados para pegar apenas os homens
    homens_df = df[df['Gênero'] == 'Masculino']

    # Crie o gráfico de pizza com Plotly Express para homens
    fig = px.pie(homens_df, names='Você costuma ler?', title='Leitura por Gênero (Homens)')

    return fig

if __name__ == '__main__':
    app.run(debug=True)
