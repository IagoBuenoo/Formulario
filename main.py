from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="feira_livre"
)

@app.route('/')
def formulario():
    return render_template('formulario.html')

@app.route('/register', methods=['POST'])
def register():
    nome = request.form['nome']
    sobrenome = request.form['sobrenome']
    email = request.form['email']
    cpf = request.form['cpf']
    escolaridade = request.form['escolaridade']
    feira = request.form['feira']
    dias = request.form.getlist('dias') 
    produtos = request.form.get('produtos')
    outros = request.form['outros']

    dias_str = ', '.join(dias)

    cursor = conexao.cursor()
    sql = """
        INSERT INTO inscricoes 
        (nome, sobrenome, email, cpf, escolaridade, feira, dias, produtos, outros)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    valores = (nome, sobrenome, email, cpf, escolaridade, feira, dias_str, produtos, outros)
    cursor.execute(sql, valores)
    conexao.commit()
    cursor.close()

    return "Inscrição realizada com sucesso!"

if __name__ == '__main__':
    app.run(debug=True)