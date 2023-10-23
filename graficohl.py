#testar estilos

from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

graphic = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.read_excel("Leituras.xlsx") 

fig = px.pie(df, names='Você costuma ler?', title='Leitura por Gênero (Homens)')

img = 'logo.png'

title_style = {
    'font-family': 'Nunito',  # Defina a fonte desejada aqui
    'font-size': '40px',  # Tamanho da fonte
    'font-weight': 'bold', # Peso da fonte (opcional)
    'color': '#28B465'
    }

graphic.layout = html.Div(
    style = {'display': 'flex', 'align-items': 'center'},
    children=[
    html.Link(
    rel='stylesheet',
    href='https://fonts.googleapis.com/css2?family=Nunito:wght@300&display=swap',
    ),
    html.Img(src=img, style={'max-width': '50px', 'height': '50px'}),
    html.H1(children='Máquina de Gráficos', style=title_style),

    dcc.Graph(
        id='grafico_leitura_genero_homens',
        figure=fig
    )
])

@graphic.callback(
    Output('grafico_leitura_genero_homens', 'figure')
   
    
)
def atualizar_grafico():
    # Filtra os dados para pegar apenas os homens
    homens_df = df[df['Genero'] == 'Masculino']

    # Crie o gráfico de pizza com Plotly Express para homens
    fig = px.pie(homens_df, names='Você costuma ler?', title='Leitura por Gênero (Homens)')

    return fig

if __name__ == '__main__':
    graphic.run(debug=True)

suppress_callback_exceptions=True 