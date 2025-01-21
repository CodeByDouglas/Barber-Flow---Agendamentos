from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from app.controllers.routes import rotas_de_adm, rotas_de_agendamento

db = SQLAlchemy()

def create_app(): 
    app = Flask(__name__)
    app.config.from_object('config.configuracao')
    db.init_app(app)

    app.register_blueprint(rotas_de_agendamento.bp)
    app.register_blueprint(rotas_de_adm.bp)

    return app