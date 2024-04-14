from app import app
from flask import render_template

@app.route('/')
@app.route('/pagina_inicial')
def pagina_inicial():
    return render_template('HomePage.html')

@app.route('/formulario')
def formulario():
    return render_template('Forms.html')

@app.route('/contato')
def contato():
    return render_template('Contato.html')

