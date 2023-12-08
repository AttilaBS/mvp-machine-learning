from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import os

# importando os elementos definidos no modelo
from model.base import Base
from model.prediction import Prediction
from model.trained_model import TrainedModel


db_path = 'database/'
if not os.path.exists(db_path):
    os.makedirs(db_path)

# url de acesso ao banco (essa é uma url de acesso ao sqlite local)
db_url = 'sqlite:///database/db.sqlite3'

#cria a engine de conexão ao banco
engine = create_engine(db_url, echo = False)

#instancia um criador de sessão com o banco
Session = sessionmaker(bind = engine)

#cria o banco se ele não existir
if not database_exists(engine.url):
    create_database(engine.url)

#cria as tabelas do banco, caso não existam
Base.metadata.create_all(engine)
