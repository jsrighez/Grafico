from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)

# Carregue os dados da planilha
df = pd.read_excel("Leitura.xlsx")

app.layout = html.Div([
    html.H1(children='Gráfico de Barras'),

    dcc.Dropdown(
        id='genero_dropdown',
        options=[
            {'label': 'Homens', 'value': 'Homens'},
            {'label': 'Mulheres', 'value': 'Mulheres'}
        ],
        value='Homens',  # Valor padrão
        multi=False
    ),

    dcc.Graph(
        id='grafico'
    )
])

@app.callback(
    Output('grafico', 'figure'),
    [Input('genero_dropdown', 'value')]
)
def criar_grafico(genero_selecionado):
    # Filtra os dados com base no gênero selecionado
    df_filtrado = df[df['Gênero'] == genero_selecionado]

    # Calcule a contagem de leitura e não leitura
    contagem_leitura = df_filtrado[df_filtrado['Você costuma ler?'] == 'Sim'].shape[0]
    contagem_nao_leitura = df_filtrado[df_filtrado['Você costuma ler?'] == 'Não'].shape[0]

    # Crie um gráfico de barras
    fig = px.bar(
        x=['Leem', 'Não Leem'],
        y=[contagem_leitura, contagem_nao_leitura],
        title=f'Leitura por {genero_selecionado}',
        labels={'x': 'Leem/Não Leem', 'y': 'Quantidade'}
    )

    return fig

if __name__ == '__main__':
    app.run(debug=True)
