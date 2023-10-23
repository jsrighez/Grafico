
#MODEL
#import psycopg2
#login
class Us:
    def __init__(self,email,senha):
        self.email = email
        self.senha = senha

#arquivo
class Arquivo:
    def __init__(self, nome_arquivo,tipo_arq):
        self.nome_arquivo = nome_arquivo
        self.tipo_arq = tipo_arq

#dados principais
class Dados_Grafico:
    def __init__(self,dado1,dado2,titulo_g,tipo_g,condicao1,condicao2):
        self.titulo_g = titulo_g
        self.tipo_g = tipo_g
        self.dado1 = dado1
        self.dado2 = dado2
        self.condicao1 = condicao1
        self.condicao2 = condicao2

#Precisa desses?
class Grafico_coluna(Dados_Grafico):
    def __init__(self,tituloc_d1,tituloc_d2):
        self.tituloc_d1 = tituloc_d1
        self.tituloc_d2 = tituloc_d2

class Grafico_barra(Dados_Grafico):
    def __init__(self,titulob_d1,titulob_d2):
        self.titulob_d1 = titulob_d1
        self.titulob_d2 = titulob_d2

class Grafico_pizza(Dados_Grafico):
    def __init__(self,titulop_d1,titulop_d2):
        self.titulop_d1 = titulop_d1
        self.titulop_d2 = titulop_d2

#Apenas uma coluna

class Grafico_coluna1(Dados_Grafico):
    def __init__(self,tituloc_d):
        self.tituloc_d = tituloc_d

class Grafico_barra1(Dados_Grafico):
    def __init__(self,titulob_d):
        self.titulob_d = titulob_d
class Grafico_pizza1(Dados_Grafico):
    def __init__(self,titulop_d):
        self.titulop_d = titulop_d
        

  

#Grafico?

#teste

from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

graphic = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.read_excel("Leitura.xlsx") 

fig = px.pie(df, names='Você costuma ler?', title='Leitura por Gênero (Homens)')

graphic.layout = html.Div(children=[
    html.H1(children='Máquina de Gráficos'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),
   
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

#---------
        
import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

# Inicialize o aplicativo Dash
app = dash.Dash(__name__)

# Dados de exemplo
df = pd.read_excel()#nome_arquivo)

# Classe para criar gráfico de barras
class GraficoDeBarras:
    def __init__(self, titulo):
        self.dados = Dadosg
        self.titulo = titulo

    def criar_grafico(self):
        fig = px.bar(self.dados, x='dado1', y='dado2', title=self.titulo)
        return fig

# Classe para criar gráfico de dispersão
class GraficoDeDispersao:
    def __init__(self, dados, titulo):
        self.dados = dados
        self.titulo = titulo

    def criar_grafico(self):
        fig = px.scatter(self.dados, x='x', y='y', title=self.titulo)
        return fig

# Layout do aplicativo
app.layout = html.Div([
    dcc.Graph(id='grafico-output'),
    dcc.Dropdown(
        id='tipo-grafico',
        options=[
            {'label': 'Gráfico de Barras', 'value': 'barras'},
            {'label': 'Gráfico de Dispersão', 'value': 'dispersao'}
        ],
        value='barras'
    )
])

# Callback para atualizar o gráfico com base no tipo selecionado
@app.callback(
    dash.dependencies.Output('grafico-output', 'figure'),
    [dash.dependencies.Input('tipo-grafico', 'value')]
)
def atualizar_grafico(tipo):
    if tipo == 'barras':
        grafico = GraficoDeBarras(df, 'Gráfico de Barras')
    else:
        grafico = GraficoDeDispersao(df, 'Gráfico de Dispersão')
    
    return grafico.criar_grafico()

if __name__ == '__main__':
    app.run_server(debug=True)
