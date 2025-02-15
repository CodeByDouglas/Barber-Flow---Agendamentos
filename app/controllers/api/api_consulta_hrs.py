from flask import Blueprint, jsonify, request
from app.utils.consulta_hrs import consultar_horarios

bp_api = Blueprint('api_consulta_hrs', __name__, url_prefix='/api')

@bp_api.route('/consulta_hrs', methods=['POST'])
def consulta_hrs():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'JSON body is required.'}), 400

    id_funcionario = data.get('id')
    dia = data.get('dia')
    mes = data.get('mes')
    ano = data.get('ano')
    admin_id = data.get('admin_id')

    if None in (id_funcionario, dia, mes, ano, admin_id):
        return jsonify({
            'error': 'Erro: Os parâmetros "id", "dia", "mes", "ano" e "admin_id" são necessários.'
        }), 400

    horarios = consultar_horarios(id_funcionario, dia, mes, ano, admin_id)
    return jsonify(horarios), 200