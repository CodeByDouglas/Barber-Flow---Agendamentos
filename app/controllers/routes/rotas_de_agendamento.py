from flask import Blueprint, render_template, redirect, url_for

bp = Blueprint('agenda', __name__)

@bp.route('/')
def index():
    return redirect(url_for('agenda.tela_inicial'))

@bp.route('/agenda')
def tela_inicial():
    return render_template('tela_inicial.html')

@bp.route('/agenda/funcionario')
def selecionar_funcionario():
    return render_template('tela_barbeiro.html')

@bp.route('/agenda/funcionario/servico')
def selecionar_servico():
    return "Selecionar Serviço"

@bp.route('/agenda/funcionario/servico/data-hora')
def selecionar_data_hora():
    return "Selecionar Data e Hora"

@bp.route('/agenda/funcionario/servico/data-hora/dado-cliente')
def coleta_dados_cliente():
    return "Coleta de Dados do Cliente"
