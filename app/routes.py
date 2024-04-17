from app import app
from flask import render_template

@app.route('/')
@app.route('/HomePage')
def HomePage():
  return render_template ('HomePage.html')

@app.route('/Forms')
def Forms():
  return render_template ('Forms.html')

@app.route('/Contato')
def Contato():
  return render_template ('Contato.html')