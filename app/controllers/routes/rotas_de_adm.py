from flask import Blueprint

bp = Blueprint('adm', __name__)

@bp.route('/adm')
def login_adm():
    return None

@bp.route('/adm/cadastro-funcionario')
def cadastrar_funcionario():
    return None

@bp.route('/adm/painel_do_funcionario')
def painel_do_funcionario():
    return None

@bp.route('/adm/painel_do_adm')
def painel_do_proprietario():
    return None