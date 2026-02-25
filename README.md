# Projeto Integrador 1 Univesp Grupo 12

🧠 Projeto Integrador 1 – UNIVESP – Grupo 12
PI Grupo 012 Projeto desenvolvido como parte da disciplina Projeto Integrador I da Universidade Virtual do Estado de São Paulo (UNIVESP)

📌 Sobre o Projeto

Este projeto integra conhecimentos adquiridos ao longo do curso de Engenharia/Computação na UNIVESP, aplicando conceitos práticos de desenvolvimento e construção de sistemas.
Ele foi criado com base em uma necessidade real ou proposta estudada pelo grupo, seguindo a metodologia do Projeto Integrador, que estimula a resolução de problemas reais com soluções aplicáveis à vida profissional do estudante universitário.

🚀 Objetivo

O objetivo principal deste repositório é apresentar uma solução técnica/software que atenda à problemática definida durante o semestre do Projeto Integrador I.
O código e a estrutura aqui presentes contemplam:

Backend em Python com Flask

Configuração de ambiente virtual Python

Banco de dados e migrações com Flask-SQLAlchemy

Scripts para execução local

Interface funcional e lógica de negócio central

🔧 Tecnologias Utilizadas

O projeto foi desenvolvido utilizando as seguintes tecnologias:

🐍 Python

🧪 Flask

🐬 Flask-SQLAlchemy

📦 Dotenv

💾 Banco de dados com SQLAlchemy

💻 HTML / CSS / JavaScript

🛠 Git & GitHub para versionamento

## Preparando o ambiente

As boas práticas de desenvolvimento em Python incentivam a criação de ambiente virtual (virtual environment) para a instalação de extensões, mantendo a instalação original do Python praticamente intacta.

### Criando um ambiente virtual

Antes de começar a instalar as extensões, é necessário criar o ambiente virtual. Para isso, é necessário rodar o seguinte comando:

```
$ python3 -m venv venv
```

Onde -m é a opção "module", seguido do nome do módulo, "venv", de "virtual environment", e depois o nome escolhido para o módulo. No exemplo, é utilizado o mesmo nome do pacote, "venv".

### Ativando o ambiente virtual

No diretório raiz do projeto, execute o seguinte comando:

Linux:

```
$ source venv/bin/activate
```

Windows:

```
$ venv\Scripts\activate
```

Windows PowerShell:

```
$ venv\Scripts\Activate.ps1
```

Após a ativação correta do ambiente virtual, o prompt de comando mostrará o ambiente virtual ativo da seguinte forma:

```
(venv) $
```

Instalando os pacotes necessários
Para executar este projeto, precisará instalar os seguintes pacotes em seu ambiente virtual:

- flask
- dotenv
- flask-sqlalchemy
- flask-migrate

Para instalar as extensões, deverá executar o seguinte comando:

```
pip install flask dotenv flask-sqlalchemy flask-migrate
```

## Inicializando o banco

Para inicializar o banco de dados, execute:

```
flask db init
```

Após a inicialização, deverá realizar a primeira migração, que criará as tabelas e colunas de acordo com os os models:

```
flask db migrate
```

Após a migração, deverá realizar o upgrade do banco para aplicar as mudanças:

```
flask db upgrade
```

## Executando a aplicação

Após conectar-se ao banco de dados, poderá executar o seguinte comando no diretório raiz do projeto:

```
flask run
```
