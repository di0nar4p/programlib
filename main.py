from flask import Flask, render_template, request
from aplicacoes import *
from flask import redirect
from templates import *

app = Flask(__name__)

@app.route('/' , methods=['GET','POST'])
def index():
    if request.method == 'POST':
        user = request.form['login']
        senha = request.form['senha']
        return acesso(user, senha)
    return render_template('login.html') 
       

@app.route('/programlibrary' , methods=['GET', 'POST'])
def programLib():
    if request.method == 'POST':
        return render_template('programs.html')
    

@app.route('/aplication/<int:x>/<int:y>/')
def aplicativo(x,y):
     return program(x,y)
 
@app.route('/aplication/par_impar/<int:n>/')
def par_ou_impar(n):
    return par_impar(n)

if __name__ == '__main__':
    app.run(debug=True)
