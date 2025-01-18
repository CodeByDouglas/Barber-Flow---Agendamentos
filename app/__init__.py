from flask import Flask 
from controllers.routes import rotas_de_adm, rotas_de_agendamento


def create_app(): 
    app = Flask(__name__)
    app.config.from_object('config')

    app.register_blueprint(rotas_de_agendamento.bp)
    app.register_blueprint(rotas_de_adm.bp)

    return app