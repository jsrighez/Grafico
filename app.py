from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def connect_db():
    return sqlite3.connect('database.db')

def init_db():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS User (ucod INTEGER PRIMARY KEY AUTOINCREMENT, email TEXT, senha TEXT)''')
    #cursor.execute('''CREATE TABLE IF NOT EXISTS Arquivo (acod INTEGER PRIMARY KEY AUTOINCREMENT, nome_arquivo TEXT, tipo_arq TEXT)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS Dados_Grafico (dgcod INTEGER PRIMARY KEY AUTOINCREMENT, titulo_g TEXT, tipo_g TEXT, dado_1 TEXT, dado_2 TEXT, condicao1 TEXT, condicao2 TEXT, acod INTEGER, FOREIGN KEY(acod) REFERENCES Arquivo(acod))''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS Grafico_pizza (pizcod INTEGER PRIMARY KEY AUTOINCREMENT, titulop_d1 TEXT, titulop_d2 TEXT, dgcodp INTEGER, FOREIGN KEY(dgcodp) REFERENCES Dados_Grafico(dgcod))''')
    conn.commit()
    conn.close()

init_db()  # Cria a tabela se ela não existir

@app.route('/', methods=['GET'])
def index():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM User")
    users = cursor.fetchall()
    conn.close()
    return render_template('index.html', Users=users)


@app.route('/Users', methods=['GET', 'POST'])
def user():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']

        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO User (email, senha) VALUES (?, ?)", (email, senha))
        conn.commit()
        conn.close()
        
        return redirect(url_for('user'))

    return render_template('t_login.html')

@app.route('/', methods=['GET'])
def index2():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Dados_Grafico")
    dados_g = cursor.fetchall()
    conn.close()
    return render_template('index2.html', Dados_g=dados_g)


@app.route('/Dados_g', methods=['GET', 'POST'])
def dados_grafico():
    if request.method == 'POST':
        titulo_g = request.form['titulo_g']
        tipo_g = request.form['tipo_g']
        dado_1 = request.form['dado_1']
        dado_2 = request.form['dado_2']
        condicao1 = request.form['condicao1']
        condicao2 = request.form['condicao2']
    
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Dados_Grafico (titulo_g, tipo_g,dado_1,dado_2, condicao1,condicao2) VALUES (?, ?,?, ?,?, ?)", (titulo_g, tipo_g,dado_1,dado_2, condicao1,condicao2))
        conn.commit()
        conn.close()
        
        return redirect(url_for('dados_g'))

    return render_template('t_escolher_input.html')

@app.route('/', methods=['GET'])
def index3():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Grafico_pizza")
    grafico_p = cursor.fetchall()
    conn.close()
    return render_template('index3.html', Grafico_p=grafico_p)


@app.route('/Grafico_p', methods=['GET', 'POST'])
def graficos_p():
    if request.method == 'POST':
        titulo_d1 = request.form['titulo_d1']
        titulo_d2 = request.form['titulo_d2']
    
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Grafico_pizza (titulo_d1, titulo_d2) VALUES (?, ?)", (titulo_d1, titulo_d2))
        conn.commit()
        conn.close()
        
        return redirect(url_for('grafico_p'))

    return render_template('t_grafico.html')

if __name__ == '__main__':
    app.run(debug=True)