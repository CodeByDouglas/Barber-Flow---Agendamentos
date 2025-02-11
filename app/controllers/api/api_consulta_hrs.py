from flask import Blueprint, jsonify, request
from app.utils.consulta_hrs import consultar_horarios

bp_api = Blueprint('api_consulta_hrs', __name__, url_prefix='/api')

@bp_api.route('/consulta_hrs', methods=['GET'])
def consulta_hrs():
    id_funcionario = request.args.get('id', type=int)
    dia = request.args.get('dia', type=int)
    mes = request.args.get('mes', type=int)
    ano = request.args.get('ano', type=int)

    if None in (id_funcionario, dia, mes, ano):
        return jsonify({'error': 'Os parâmetros "id", "dia", "mes" e "ano" são necessários.'}), 400

    horarios = consultar_horarios(id_funcionario, dia, mes, ano)
    return jsonify(horarios), 200