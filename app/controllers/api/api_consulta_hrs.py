from flask import Blueprint, jsonify, request
from app.utils.consulta_hrs import consultar_horarios

bp_api = Blueprint('api_consulta_hrs', __name__, url_prefix='/api')

@bp_api.route('/consulta_hrs', methods=['GET'])
def consulta_hrs():
    id_funcionario = request.args.get('id', type=int)
    dia = request.args.get('dia', type=int)
    mes = request.args.get('mes', type=int)
    ano = request.args.get('ano', type=int)
    admin_id = request.args.get('admin_id')

    if None in (id_funcionario, dia, mes, ano, admin_id):
        return jsonify({'error': 'Os parâmetros "id", "dia", "mes", "ano" e "admin_id" são necessários.'}), 400

    horarios = consultar_horarios(id_funcionario, dia, mes, ano, admin_id)
    return jsonify(horarios), 200