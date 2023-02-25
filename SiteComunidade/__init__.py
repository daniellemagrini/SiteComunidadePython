from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os
import sqlalchemy


app = Flask(__name__)

app.config['SECRET_KEY'] = 'b351dd056cdced1bf6164b8455f4453c'
if os.getenv("DATABASE_URL"): #Caso esteja rodando no servidor
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Comunidade.db'

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Favor realizar o login para a página ser liberada'
login_manager.login_message_category = 'alert-info'

from SiteComunidade import models
engine = sqlalchemy.create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
if not engine.dialect.has_table(engine,"usuario"):
    with app.app_context():
        database.drop_all()
        database.create_all()
        print("Base de dados criada com sucesso!")
else:
    print("Base de dados já existente")

from SiteComunidade import routes
