from app import app, db
from flask import render_template, request, redirect
from app.models import Candidato


@app.route('/')
@app.route('/HomePage')
def HomePage():
  return render_template ('HomePage.html')

@app.route('/Forms', methods=['GET', 'POST'])
def Forms():
  if request.method == 'POST':
    nome = request.form['nome_c']
    data = request.form['data_nasc']
    email = request.form['email']
    contato = request.form['telefone']

    candidato = Candidato(
      nome=nome,
      nasc=data,
      email=email,
      contato=contato
    )

    db.session.add(candidato)
    db.session.commit()

    return redirect('/Forms')

  return render_template ('Forms.html')

@app.route('/Contato')
def Contato():

  return render_template ('Contato.html')

