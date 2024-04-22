import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    # ...placeholder para outras configurações
    # CONFIG_1 =
    # CONFIG_2 =

    # !!! Ainda será preciso configurar a conexão com mariadb
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')