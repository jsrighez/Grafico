# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.


from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

graphic = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.read_excel("Leitura.xlsx") 

fig = px.pie(df, names='Você costuma baixar PDF de livros não autorizados?', title='PDF')

graphic.layout = html.Div(children=[
    html.H1(children='Máquina de Gráficos'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    dcc.Graph(
        id='grafico_leitura_genero',
        figure=fig
    )
])

@graphic.callback(
    Output('grafico_leitura_genero', 'figure')
)

def criar_grafico():
    # Filtra os dados para pegar apenas as linhas onde 'Você costuma baixar PDF de livros não autorizados?' não é igual a 'null'
    df_filtrado = df[df['Você costuma baixar PDF de livros não autorizados?'] != 'null']
    #não deu certo

    # Crie o gráfico de pizza com Plotly Express
    fig = px.pie(df_filtrado, names='Você costuma baixar PDF de livros não autorizados?', title='PDF')

    return fig

if __name__ == '__main__':
    graphic.run(debug=True)





