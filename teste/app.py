# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.


from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.read_excel("Vendas.xlsx")

fig = px.bar(df, x="Produto", y="Quantidade", color="ID Loja", barmode="group")
options = list(df['ID Loja'].unique())
options.append("Todas as lojas")

url = "https://www.youtube.com/"
#url = "file:///C:/Users/User/Documents/3%C2%BA%20ano%20EM%202023%20CETEC/T%C3%A9cnico%20em%20Inform%C3%A1tica/Programa%C3%A7%C3%A3o%20II/Prog/Graficos/Graficos/t_login.html"


local_html_path = "file:///C:/Users/User/Documents/3%C2%BA%20ano%20EM%202023%20CETEC/T%C3%A9cnico%20em%20Inform%C3%A1tica/Programa%C3%A7%C3%A3o%20II/Prog/Graficos/Graficos/t_login.html"
link_text =  "Ir para tela de login"

#problema


app.layout = html.Div(children=[
    html.H1(children='Máquina de Gráficos'),
    html.A(link_text, href=local_html_path, target="_blank"),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),
   
    dcc.Dropdown(options, value = 'Todas as lojas', id='lista_lojas'),
    dcc.Graph(
        id='grafico_quantidade_vendas',
        figure=fig
    )
])

@app.callback(
    Output('grafico_quantidade_vendas', 'figure'),
    Input('lista_lojas', 'value')
)
def update_output(value):
    if value == "Todas as lojas":
        fig = px.bar(df, x="Produto", y="Quantidade", color="ID Loja", barmode="group")
    else:
        tabela_filt = df.loc[df["ID Loja"] == value, :]
        fig = px.bar(tabela_filt, x="Produto", y="Quantidade", color="ID Loja", barmode="group")
    return fig

if __name__ == '__main__':
    app.run(debug=True)
