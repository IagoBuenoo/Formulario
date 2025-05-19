from flask import Flask, render_template, request, redirect
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)
def connect_db():
    try:
        conn = mysql.connector.connect(
            host='localhost',
            database='feira',
            user='root',
            password='root'
        )
        if conn.is_connected():
            print('Conectado ao banco de dados MySQL')
        return conn
    except Error:
        print(f"Erro")
        return None
def create_table():
    connect = connect_db()
    if connect:
        cursor = connect.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS inscricoes (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(255),
                sobrenome VARCHAR(255),
                email VARCHAR(255),
                cpf VARCHAR(255),
                escolaridade VARCHAR(255),
                produtos VARCHAR(255),
                outros TEXT
            )
        ''')
        connect.commit()
        cursor.close()
        connect.close()
        print("Tabela criada ou já existente.")
    else:
        print("Falha na conexão do banco de dados.")

create_table()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    nome = request.form['nome']
    sobrenome = request.form['sobrenome']
    email = request.form['email']
    cpf = request.form['cpf']
    escolaridade = request.form['escolaridade']
    produtos = request.form.get('produtos')
    outros = request.form['outros']

    connect = connect_db()
    if connect:
        cursor = connect.cursor()
        cursor.execute('''
            INSERT INTO inscricoes (nome, sobrenome, email, cpf, escolaridade, produtos, outros)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        ''', (nome, sobrenome, email, cpf, escolaridade, produtos, outros))
        connect.commit()
        cursor.close()
        connect.close()
        print("Dados inseridos com sucesso.")
    else:
        print("Falha na conexão do banco de dados.")

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)