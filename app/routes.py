from app import app, db
from flask import render_template, request
from app.models import Candidato, FaleConosco

@app.route('/')
@app.route('/HomePage')
def HomePage():
  return render_template ('HomePage.html')

@app.route('/Forms', methods=['GET', 'POST'])
def Forms():
  if request.method == 'POST':
    nome = request.form['nome_c']
    email = request.form['email']
    telefone = request.form['telefone']
    endereco = request.form['endereco']
    objetivo = request.form['objetivo']
    formacao = request.form['formação']
    xp = request.form['experiencia']

    candidato = Candidato(
      nome=nome,
      email=email,
      telefone=telefone,
      endereco=endereco,
      objetivo=objetivo,
      formacao=formacao,
      experiencia=xp
    )

    db.session.add(candidato)
    db.session.commit()

  return render_template ('Forms.html')

@app.route('/Contato', methods=['GET', 'POST'])
def Contato():
  if request.method == 'POST':
    nome_contato = request.form['nome']
    email = request.form['email']
    telefone = request.form['telefone']
    endereco = request.form['endereco']
    estado = request.form['estado']
    cidade = request.form['cidade']
    mensagem = request.form['mensagem']

    contato = FaleConosco(
      nome_contato=nome_contato,
      email_contato=email,
      telefone_contato=telefone,
      endereco_contato=endereco,
      estado=estado,
      cidade=cidade,
      mensagem=mensagem
    )

    db.session.add(contato)
    db.session.commit()

  return render_template ('Contato.html')