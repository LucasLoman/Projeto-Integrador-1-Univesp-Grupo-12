# ".\venv\Scripts\activate" Para ligar o ambiente virtual
from flask import Flask
app= Flask(__name__)
from app import routes
