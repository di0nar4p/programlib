from flask import Flask, render_template
from home import home
from aplicacoes import *

app = Flask(__name__)

@app.route('/home')
def index():
    return home()

@app.route('/aplication/<int:x>/<int:y>/')
def aplicativo(x,y):

     return program(x,y)
 
@app.route('/aplication/par_impar/<int:n>/')
def par_ou_impar(n):
    return par_impar(n)

@app.route('/about')
def info():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)