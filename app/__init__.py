from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    flask_app = Flask(__name__)
    flask_app.config.from_object('config.configuracao')
    db.init_app(flask_app)

    with flask_app.app_context():
        import app.models

    from app.controllers.routes import rotas_de_adm, rotas_de_agendamento
    flask_app.register_blueprint(rotas_de_agendamento.bp)
    flask_app.register_blueprint(rotas_de_adm.bp)
    
    # Registra o blueprint da API
    from app.controllers.api import api_create_hrs
    flask_app.register_blueprint(api_create_hrs.bp_api)

    return flask_app