import psycopg2

# Dados da conexão
HOST = "ep-fancy-frog-58641694-pooler.us-east-1.postgres.vercel-storage.com"
DATA_BASE = "verceldb"
USER = "default"
PASS = "xXxXxXxXxXxXxXxXxXxXxXxXxXxXx"

class Us:
    def __init__(self,ucod,email,senha):
        self.ucod = ucod
        self.email = email
        self.senha = senha

#arquivo
class Arquivo:
    def __init__(self, acod,nome_arquivo,tipo_arq):
        self.acod = acod
        self.nome_arquivo = nome_arquivo
        self.tipo_arq = tipo_arq

#dados principais
class Dados_Grafico:
    def __init__(self,acod,dado1,dado2,titulo_g,tipo_g,condicao1,condicao2):
        self.titulo_g = titulo_g
        self.tipo_g = tipo_g
        self.dado1 = dado1
        self.dado2 = dado2
        self.condicao1 = condicao1
        self.condicao2 = condicao2
        self.acod = acod

#Precisa desses?
class Grafico_coluna(Dados_Grafico):
    def __init__(self,tituloc_d1,tituloc_d2,dgcodc, colcod):
        self.colcod = colcod
        self.tituloc_d1 = tituloc_d1
        self.tituloc_d2 = tituloc_d2
        self.dgcodc = dgcodc

class Grafico_barra(Dados_Grafico):
    def __init__(self,titulob_d1,titulob_d2,dgcodb, barcod):
        self.titulob_d1 = titulob_d1
        self.barcod = barcod
        self.titulob_d2 = titulob_d2
        self.dgcodb = dgcodb


class Grafico_pizza(Dados_Grafico):
    def __init__(self,titulop_d1,titulop_d2,dgcodp, pizcod):
        self.pizcod = pizcod
        self.titulop_d1 = titulop_d1
        self.titulop_d2 = titulop_d2
        self.dgcodp = dgcodp

#Apenas uma coluna

class Grafico_coluna1(Dados_Grafico):
    def __init__(self,tituloc_d, col1cod,dgcodc1):
        self.tituloc_d = tituloc_d
        self.col1cod = col1cod
        self.dgcodc1 = dgcodc1

class Grafico_barra1(Dados_Grafico):
    def __init__(self,titulob_d,bar1cod,dgcodb1):
        self.titulob_d = titulob_d
        self.bar1cod = bar1cod
        self.dgcodb1 = dgcodb1


class Grafico_pizza1(Dados_Grafico):
    def __init__(self,titulop_d,piz1cod,dgcodp1):
        self.titulop_d = titulop_d
        self.piz1cod = piz1cod
        self.dgcodp1 = dgcodp1
        

def create_table():
    try:
        # Conecta no banco de dados
        conn = psycopg2.connect(
            host=HOST,
            database=DATA_BASE,
            user=USER,
            password=PASS
        )

        # Cria a tabela
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS us (
                ucod SERIAL PRIMARY KEY,
                email varchar(50) NOT NULL,
                senha varchar(10) NOT NULL
            )
        """)
        conn.commit()
        print("Tabela usuário criada com sucesso!")

        # Cria a tabela
        x = conn.cursor()
        x.execute("""
            CREATE TABLE IF NOT EXISTS Arquivo (
                acod SERIAL PRIMARY KEY,
                nome_arquivo VARCHAR(50) NOT NULL,
                tipo_arq VARCHAR(4) NOT NULL
            )
        """)
        conn.commit()
        print("Tabela Arquivo criada com sucesso!")

        # Cria a tabela post
        y = conn.cursor()
        y.execute("""
            CREATE TABLE IF NOT EXISTS Dados_Graficos (
                dgcod INTEGER NOT NULL,
                titulo_g VARCHAR(50) NOT NULL,
                tipo_g VARCHAR (6) NOT NULL,
                dado_1 VARCHAR (100) NOT NULL,
                dado_2 VARCHAR DEFAULT 's',
                condicao1 VARCHAR (50) NOT NULL,
                condicao2 VARCHAR(50),
                acod INTEGER NOT NULL,
                PRIMARY KEY(dgcod,acod),
                FOREIGN KEY(acod) REFERENCES Arquivo(acod)
            )
        """)
        conn.commit()
        print("Tabela Dados_Grafico criada com sucesso!")

        z = conn.cursor()
        z.execute("""
            CREATE TABLE IF NOT EXISTS Grafico_coluna (
                colcod INTEGER NOT NULL,
                tituloc_d1 VARCHAR(50),
                tituloc_d2 VARCHAR (50),
                dgcodc INTEGER,
                PRIMARY KEY(colcod,dgcod),
                FOREIGN KEY(dgcodc) REFERENCES Dados_Grafico(dgcod)
          )
        """)
        conn.commit()
        print("Tabela Grafico_coluna criada com sucesso!")

        a = conn.cursor()
        a.execute("""
            CREATE TABLE IF NOT EXISTS Grafico_barra (
                barcod INTEGER NOT NULL,
                titulob_d1 VARCHAR(50),
                titulob_d2 VARCHAR(50),
                dgcodb INTEGER,
                PRIMARY KEY(barcod,dgcodb),
                FOREIGN KEY(dgcodb) REFERENCES Dados_Grafico(dgcod)
            )
        """)
        conn.commit()
        print("Tabela Grafico_barra criada com sucesso!")

        b= conn.cursor()
        b.execute("""
            CREATE TABLE IF NOT EXISTS Grafico_pizza (
                pizcod INTEGER NOT NULL,
                titulop_d1 VARCHAR(50),
                titulop_d2 VARCHAR(50),
                dgcodp INTEGER,
                PRIMARY KEY(pizcod,dgcodp),
                FOREIGN KEY(dgcodp) references Dados_Grafico(dgcod)
            )
        """)
        conn.commit()
        print("Tabela Grafico_pizza criada com sucesso!")

        c= conn.cursor()
        c.execute("""
            CREATE TABLE IF NOT EXISTS Grafico_coluna1 (
                col1cod INTEGER NOT NULL,
                tituloc_d1 VARCHAR(50),
                dgcodc1 INTEGER,
                PRIMARY KEY(col1cod,dgcod),
                FOREIGN KEY(dgcodc1) REFERENCES Dados_Grafico(dgcod)
            )
        """)
        conn.commit()
        print("Tabela Grafico_coluna1 criada com sucesso!")

        d= conn.cursor()
        d.execute("""
            CREATE TABLE IF NOT EXISTS Grafico_barra1 (
                bar1cod INTEGER NOT NULL,
                titulob_d1 VARCHAR(50),
                dgcodb1 INTEGER,
                PRIMARY KEY(bar1cod,dgcodb1),
                FOREIGN KEY(dgcodb1) REFERENCES Dados_Grafico(dgcod)
            )
        """)
        conn.commit()
        print("Tabela Grafico_barra1 criada com sucesso!")

        e= conn.cursor()
        e.execute("""
            CREATE TABLE IF NOT EXISTS Grafico_pizza1 (
                piz1cod INTEGER NOT NULL,
                titulop_d1 VARCHAR(50),
                dgcodp1 INTEGER,
                PRIMARY KEY(piz1cod,dgcodp1),
                FOREIGN KEY(dgcodp1) REFERENCES Dados_Grafico(dgcod)
            )
        """)
        conn.commit()
        print("Tabela Grafico_pizza1 criada com sucesso!")

    except psycopg2.Error as e:
        print("Erro ao criar tabela:", e)

    finally:
        # Fecha a conexão
        if conn is not None:
            conn.close()

def insert_us(us):
    try:
        # Conecta no banco de dados
        conn = psycopg2.connect(
            host=HOST,
            database=DATA_BASE,
            user=USER,
            password=PASS
        )

        # Insere o usuário na tabela
        cur = conn.cursor()
        cur.execute("INSERT INTO us (ucod, email, senha) VALUES (%s, %s,%s)", (us.ucod, us.email,us.senha))
        conn.commit()
        print("Usuário inserido com sucesso!")

    except psycopg2.Error as e:
        print("Erro ao inserir usuário:", e)

    finally:
        # Fecha a conexão
        if conn is not None:
            conn.close()

def insert_arquivo(arq):
    try:
        # Conecta no banco de dados
        conn = psycopg2.connect(
            host=HOST,
            database=DATA_BASE,
            user=USER,
            password=PASS
        )

        # Insere o usuário na tabela
        cur = conn.cursor()
        cur.execute("INSERT INTO Arquivo (acod,nome_arquivo, tipo_arq) VALUES (%s, %s, %s)", (arq.acod, arq.nome_arquivo, arq.tipo_arq))
        conn.commit()
        print("Arquivo inserido com sucesso!")

    except psycopg2.Error as e:
        print("Erro ao inserir Arquivo:", e)

    finally:
        # Fecha a conexão
        if conn is not None:
            conn.close()

def insert_dados_grafico(dg):
    try:
        # Conecta no banco de dados
        conn = psycopg2.connect(
            host=HOST,
            database=DATA_BASE,
            user=USER,
            password=PASS
        )

        # Insere o usuário na tabela
        cur = conn.cursor()
        cur.execute("INSERT INTO Dados_Grafico (dgcod, titulo_g, tipo_g, dado_1, dado_2,condicao1,condicao2,acod) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (dg.dgcod, dg.titulo_g, dg.tipo_g, dg.dado_1, dg.dado_2,dg.condicao1,dg.condicao2,dg.acod))
        conn.commit()
        print("dg inserido com sucesso!")

    except psycopg2.Error as e:
        print("Erro ao inserir dg:", e)

    finally:
        # Fecha a conexão
        if conn is not None:
            conn.close()

def insert_grafico_coluna(gc):
    try:
        # Conecta no banco de dados
        conn = psycopg2.connect(
            host=HOST,
            database=DATA_BASE,
            user=USER,
            password=PASS
        )

        # Insere o usuário na tabela
        cur = conn.cursor()
        cur.execute("INSERT INTO Grafico_coluna (colcod, tituloc_d1, tituloc_d2, dgcodc) VALUES (%s, %s, %s, %s)", (gc.colcod, gc.tituloc_d1, gc.tituloc_d2, gc.dgcodc))
        conn.commit()
        print("gc inserido com sucesso!")

    except psycopg2.Error as e:
        print("Erro ao inserir gc:", e)

    finally:
        # Fecha a conexão
        if conn is not None:
            conn.close()

def insert_grafico_barra(gb):
    try:
        # Conecta no banco de dados
        conn = psycopg2.connect(
            host=HOST,
            database=DATA_BASE,
            user=USER,
            password=PASS
        )

        # Insere o usuário na tabela
        cur = conn.cursor()
        cur.execute("INSERT INTO Grafico_barra (barcod, titulob_d1, titulob_d2, dgcodb) VALUES (%s, %s, %s, %s)", (gb.barcod, gb.titulob_d1, gb.tipob_d2, gb.dgcodb))
        conn.commit()
        print("gb inserido com sucesso!")

    except psycopg2.Error as e:
        print("Erro ao inserir gb:", e)

    finally:
        # Fecha a conexão
        if conn is not None:
            conn.close()



def insert_grafico_pizza(gp):
    try:
        # Conecta no banco de dados
        conn = psycopg2.connect(
            host=HOST,
            database=DATA_BASE,
            user=USER,
            password=PASS
        )

        # Insere o usuário na tabela
        cur = conn.cursor()
        cur.execute("INSERT INTO Grafico_pizza (pizcod, titulop_d1, titulop_d2, dgcodp) VALUES (%s, %s, %s, %s)", (gp.pizcod, gp.titulop_d1, gp.titulop_d2, gp.dgcodp))
        conn.commit()
        print("gp inserido com sucesso!")

    except psycopg2.Error as e:
        print("Erro ao inserir gp:", e)

    finally:
        # Fecha a conexão
        if conn is not None:
            conn.close()

def insert_grafico_coluna1(gc1):
    try:
        # Conecta no banco de dados
        conn = psycopg2.connect(
            host=HOST,
            database=DATA_BASE,
            user=USER,
            password=PASS
        )

        # Insere o usuário na tabela
        cur = conn.cursor()
        cur.execute("INSERT INTO Grafico_coluna1 (col1cod, tituloc_d1, dgcodc1) VALUES (%s, %s, %s)", (gc1.col1cod, gc1.tituloc_d1, gc1.dgcodc1))
        conn.commit()
        print("gc1 inserido com sucesso!")

    except psycopg2.Error as e:
        print("Erro ao inserir gc1:", e)

    finally:
        # Fecha a conexão
        if conn is not None:
            conn.close()

def insert_grafico_barra1(gb1):
    try:
        # Conecta no banco de dados
        conn = psycopg2.connect(
            host=HOST,
            database=DATA_BASE,
            user=USER,
            password=PASS
        )

        # Insere o usuário na tabela
        cur = conn.cursor()
        cur.execute("INSERT INTO Grafico_barra1 (bar1cod, titulob_d1, dgcodb1) VALUES (%s, %s, %s)", (gb1.bar1cod, gb1.titulob_d1, gb1.dgcodb1))
        conn.commit()
        print("gb1 inserido com sucesso!")

    except psycopg2.Error as e:
        print("Erro ao inserir gb1:", e)

    finally:
        # Fecha a conexão
        if conn is not None:
            conn.close()

def insert_grafico_pizza1(gp1):
    try:
        # Conecta no banco de dados
        conn = psycopg2.connect(
            host=HOST,
            database=DATA_BASE,
            user=USER,
            password=PASS
        )

        # Insere o usuário na tabela
        cur = conn.cursor()
        cur.execute("INSERT INTO Grafico_pizza1 (piz1cod, titulop_d1, dgcodp1) VALUES (%s, %s, %s)", (gp1.bar1cod, gp1.titulob_d1, gp1.dgcodb1))
        conn.commit()
        print("gp1 inserido com sucesso!")

    except psycopg2.Error as e:
        print("Erro ao inserir gp1:", e)

    finally:
        # Fecha a conexão
        if conn is not None:
            conn.close()

            #select

def select_us():
    try:
        # Conecta no banco de dados
        conn = psycopg2.connect(
            host=HOST,
            database=DATA_BASE,
            user=USER,
            password=PASS
        )

        # Seleciona todos os usuários da tabela
        cur = conn.cursor()
        cur.execute("SELECT * FROM us")
        rows = cur.fetchall()

        # Exibe os usuários na tela
        for row in rows:
            us = Us(row[0], row[1], row[2])
            print(f"Código: {us.ucod}, Email: {us.email}, Senha: {us.senha}")

    except psycopg2.Error as e:
        print("Erro ao selecionar usuários:", e)

    finally:
        # Fecha a conexão
        if conn is not None:
            conn.close()


def select_arquivo():
    try:
        # Conecta no banco de dados
        conn = psycopg2.connect(
            host=HOST,
            database=DATA_BASE,
            user=USER,
            password=PASS
        )

        # Seleciona todos os usuários da tabela
        cur = conn.cursor()
        cur.execute("SELECT * FROM Arquivo")
        rows = cur.fetchall()

        # Exibe os usuários na tela
        for row in rows:
            arq = Arquivo(row[0], row[1], row[2], row[3], row[4], row[5])
            print(f"Código: {arq.acod}, Nome: {arq.nome_arquivo}, Tipo: {arq.tipo_arq}")

    except psycopg2.Error as e:
        print("Erro ao selecionar usuários:", e)

    finally:
        # Fecha a conexão
        if conn is not None:
            conn.close()


def select_Dados_grafico():
    try:
        # Conecta no banco de dados
        conn = psycopg2.connect(
            host=HOST,
            database=DATA_BASE,
            user=USER,
            password=PASS
        )

        # Seleciona todos os usuários da tabela
        cur = conn.cursor()
        cur.execute("SELECT * FROM Dados_Graficos")
        rows = cur.fetchall()

        # Exibe os usuários na tela
        for row in rows:
            dg = Dados_Grafico(row[0], row[1], row[2], row[3], row[4])
            print(f"Código: {dg.dgcod}, Título gráfico: {dg.titulo_g}, Tipo do Gráfico: {dg.tipo_g}, Dado 1: {dg.dado_1}, Dado 2: {dg.dado_2}, Condição 1: {dg.condicao1}, Condição 2: {dg.condicao2}, Acod: {dg.acod}")

    except psycopg2.Error as e:
        print("Erro ao selecionar dados_grafico:", e)

    finally:
        # Fecha a conexão
        if conn is not None:
            conn.close()

def select_Grafico_coluna():
    try:
        # Conecta no banco de dados
        conn = psycopg2.connect(
            host=HOST,
            database=DATA_BASE,
            user=USER,
            password=PASS
        )

        # Seleciona todos os usuários da tabela
        cur = conn.cursor()
        cur.execute("SELECT * FROM Grafico_coluna")
        rows = cur.fetchall()

        # Exibe os usuários na tela
        for row in rows:
            gc = Grafico_coluna(row[0], row[1], row[2], row[3], row[4])
            print(f"Código: {gc.colcod}, Título dado 1: {gc.tituloc_d1}, Tipo dado 2: {gc.tituloc_d2}, Código dado-gráfico: {gc.gcodc}")

    except psycopg2.Error as e:
        print("Erro ao selecionar usuários:", e)

    finally:
        # Fecha a conexão
        if conn is not None:
            conn.close()

def select_Grafico_barra():
    try:
        # Conecta no banco de dados
        conn = psycopg2.connect(
            host=HOST,
            database=DATA_BASE,
            user=USER,
            password=PASS
        )

        # Seleciona todos os usuários da tabela
        cur = conn.cursor()
        cur.execute("SELECT * FROM Grafico_barra")
        rows = cur.fetchall()

        # Exibe os usuários na tela
        for row in rows:
            gb = Grafico_barra(row[0], row[1], row[2], row[3], row[4])
            print(f"Código: {gb.barcod}, Título dado 1: {gb.titulob_d1}, Tipo dado 2: {gb.titulob_d2}, Código dado-gráfico: {gb.gcodb}")

    except psycopg2.Error as e:
        print("Erro ao selecionar usuários:", e)

    finally:
        # Fecha a conexão
        if conn is not None:
            conn.close()

def select_Grafico_pizza():
    try:
        # Conecta no banco de dados
        conn = psycopg2.connect(
            host=HOST,
            database=DATA_BASE,
            user=USER,
            password=PASS
        )

        # Seleciona todos os usuários da tabela
        cur = conn.cursor()
        cur.execute("SELECT * FROM Grafico_pizza")
        rows = cur.fetchall()

        # Exibe os usuários na tela
        for row in rows:
            gp = Grafico_pizza(row[0], row[1], row[2], row[3], row[4])
            print(f"Código: {gp.pizcod}, Título dado 1: {gp.titulop_d1}, Tipo dado 2: {gp.titulop_d2}, Código dado-gráfico: {gp.dgcodp}")

    except psycopg2.Error as e:
        print("Erro ao selecionar usuários:", e)

    finally:
        # Fecha a conexão
        if conn is not None:
            conn.close()

def select_Grafico_coluna1():
    try:
        # Conecta no banco de dados
        conn = psycopg2.connect(
            host=HOST,
            database=DATA_BASE,
            user=USER,
            password=PASS
        )

        # Seleciona todos os usuários da tabela
        cur = conn.cursor()
        cur.execute("SELECT * FROM Grafico_coluna1")
        rows = cur.fetchall()

        # Exibe os usuários na tela
        for row in rows:
            gc1 = Grafico_coluna1(row[0], row[1], row[2], row[3], row[4])
            print(f"Código: {gc1.col1cod}, Título dado 1: {gc1.tituloc_d1}, Código dado-gráfico: {gc1.dgcodc1}")

    except psycopg2.Error as e:
        print("Erro ao selecionar usuários:", e)

    finally:
        # Fecha a conexão
        if conn is not None:
            conn.close()

def select_Grafico_barra1():
    try:
        # Conecta no banco de dados
        conn = psycopg2.connect(
            host=HOST,
            database=DATA_BASE,
            user=USER,
            password=PASS
        )

        # Seleciona todos os usuários da tabela
        cur = conn.cursor()
        cur.execute("SELECT * FROM Grafico_barra1")
        rows = cur.fetchall()

        # Exibe os usuários na tela
        for row in rows:
            gb1 = Grafico_barra1(row[0], row[1], row[2], row[3], row[4])
            print(f"Código: {gb1.bar1cod}, Título dado 1: {gb1.titulob_d1}, Código dado-gráfico: {gb1.dgcodb1}")

    except psycopg2.Error as e:
        print("Erro ao selecionar usuários:", e)

    finally:
        # Fecha a conexão
        if conn is not None:
            conn.close()

def select_Grafico_pizza1():
    try:
        # Conecta no banco de dados
        conn = psycopg2.connect(
            host=HOST,
            database=DATA_BASE,
            user=USER,
            password=PASS
        )

        # Seleciona todos os usuários da tabela
        cur = conn.cursor()
        cur.execute("SELECT * FROM Grafico_pizza1")
        rows = cur.fetchall()

        # Exibe os usuários na tela
        for row in rows:
            gp1 = Grafico_pizza1(row[0], row[1], row[2], row[3], row[4])
            print(f"Código: {gp1.piz1cod}, Título dado 1: {gp1.titulop_d1}, Tipo dado 2: {gp1.tituloc_d2}, Código dado-gráfico: {gp1.dgcodp1}")

    except psycopg2.Error as e:
        print("Erro ao selecionar usuários:", e)

    finally:
        # Fecha a conexão
        if conn is not None:
            conn.close()

# Cria a tabela
create_table()

'''# Insere um usuário
us = Us(None, "Aluno nota 10", "alunonota10@example.com")
insert_us(us)

# id, processo, data, descricao, status
ar = Arquivo(None, "Processo 1", "01/01/2021", "Teste", True)
insert_arquivo(ar)

# self, id, title, content, user_id, status, data):
dg = Dados_Grafico(None, "Post 2", "Esse dia foi louco",1, True, "01/01/2021")
insert_dados_grafico(dg)

# Seleciona todos os usuários e exibe na tela
select_us()
select_a()
select_posts()'''