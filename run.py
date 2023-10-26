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
        print("Tabela criada com sucesso!")

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
        print("Tabela Processo criada com sucesso!")

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
        print("Tabela Post criada com sucesso!")

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
        print("Tabela Post criada com sucesso!")

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
        print("Tabela Post criada com sucesso!")

        b= conn.cursor()
        b.execute("""
            CREATE TABLE IF NOT EXISTS Grafico_pizza (
                pizcod INTEGER NOT NULL,
                titulocp_d1 VARCHAR(50),
                titulop_d2 VARCHAR(50),
                dgcodp INTEGER,
                PRIMARY KEY(pizcod,dgcodp),
                FOREIGN KEY(dgcodp) references Dados_Grafico(dgcod)
            )
        """)
        conn.commit()
        print("Tabela Processo criada com sucesso!")

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
        print("Tabela Processo criada com sucesso!")

        d= conn.cursor()
        d.execute("""
            CREATE TABLE IF NOT EXISTS Grafico_barra1 (
                bar1cod INTEGER NOT NULL,
                tituloc_d1 VARCHAR(50),
                dgcodb1 INTEGER,
                PRIMARY KEY(bar1cod,dgcodb1),
                FOREIGN KEY(dgcodb1) REFERENCES Dados_Grafico(dgcod)
            )
        """)
        conn.commit()
        print("Tabela Processo criada com sucesso!")

        e= conn.cursor()
        e.execute("""
            CREATE TABLE IF NOT EXISTS Grafico_pizza1 (
                piz1cod INTEGER NOT NULL,
                tituloc_d1 VARCHAR(50),
                dgcodp1 INTEGER,
                PRIMARY KEY(piz1cod,dgcodp1),
                FOREIGN KEY(dgcodp1) REFERENCES Dados_Grafico(dgcod)
            )
        """)
        conn.commit()
        print("Tabela Processo criada com sucesso!")

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
        cur.execute("INSERT INTO processos (processo, data, descricao, status) VALUES (%s, %s, %s, %s)", (arq.processo, proc.data, proc.descricao, proc.status))
        conn.commit()
        print("Processo inserido com sucesso!")

    except psycopg2.Error as e:
        print("Erro ao inserir processo:", e)

    finally:
        # Fecha a conexão
        if conn is not None:
            conn.close()

def insert_post(post):
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
        cur.execute("INSERT INTO posts (title, datapost, content, status, user_id) VALUES (%s, %s, %s, %s, %s)", (post.title, post.datapost, post.content, post.status, post.user_id))
        conn.commit()
        print("Post inserido com sucesso!")

    except psycopg2.Error as e:
        print("Erro ao inserir post:", e)

    finally:
        # Fecha a conexão
        if conn is not None:
            conn.close()


def select_users():
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
        cur.execute("SELECT * FROM users")
        rows = cur.fetchall()

        # Exibe os usuários na tela
        for row in rows:
            user = User(row[0], row[1], row[2])
            print(f"ID: {user.id}, Nome: {user.name}, Email: {user.email}")

    except psycopg2.Error as e:
        print("Erro ao selecionar usuários:", e)

    finally:
        # Fecha a conexão
        if conn is not None:
            conn.close()

def select_posts():
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
        cur.execute("SELECT * FROM posts")
        rows = cur.fetchall()

        # Exibe os usuários na tela
        for row in rows:
            post = Post(row[0], row[1], row[2], row[3], row[4], row[5])
            print(f"ID: {post.id}, Conteúdo: {post.content}, Data: {post.datapost}, Status: {post.status}, User_id: {post.user_id}")

    except psycopg2.Error as e:
        print("Erro ao selecionar usuários:", e)

    finally:
        # Fecha a conexão
        if conn is not None:
            conn.close()


def select_processos():
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
        cur.execute("SELECT * FROM processos")
        rows = cur.fetchall()

        # Exibe os usuários na tela
        for row in rows:
            proc = Processo(row[0], row[1], row[2], row[3], row[4])
            print(f"ID: {user.id}, Processo: {proc.descricao}, Data: {proc.data}")

    except psycopg2.Error as e:
        print("Erro ao selecionar usuários:", e)

    finally:
        # Fecha a conexão
        if conn is not None:
            conn.close()

# Cria a tabela
create_table()

# Insere um usuário
us = Us(None, "Aluno nota 10", "alunonota10@example.com")
insert_user(us)

# id, processo, data, descricao, status
ar = Arquivo(None, "Processo 1", "01/01/2021", "Teste", True)
insert_arquivo(ar)

# self, id, title, content, user_id, status, data):
dg = Dados_Grafico(None, "Post 2", "Esse dia foi louco",1, True, "01/01/2021")
insert_post(dg)

# Seleciona todos os usuários e exibe na tela
select_us()
select_a()
select_posts()