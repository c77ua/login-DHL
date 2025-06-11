from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('cadastro.html')

@app.route('/cadastro', methods=['POST'])
def cadastro():
    nome = request.form['nome']
    email = request.form['email']
    senha = request.form['senha']
    
    print(f'Nome: {nome}, Email: {email}, Senha: {senha}')
    
    return f'<h3>Cadastro realizado com sucesso para {nome}!</h3>'

if __name__ == '__main__':
    app.run(debug=True)
