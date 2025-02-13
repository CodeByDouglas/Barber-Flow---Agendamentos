from flask import Blueprint, request, jsonify
from app.utils.create_hrs import gerar_horarios_proximo_mes


bp_api = Blueprint('api_create_hrs', __name__, url_prefix='/api')

@bp_api.route('/create-hrs', methods=['POST'])
def create_hrs():
    data = request.get_json()
    admin_id = data.get('admin_id')
    if not admin_id:
        return jsonify({'error': 'admin_id is required'}), 400

    resultado = gerar_horarios_proximo_mes(admin_id)
    
    # Se ocorrer um erro, retorna status 500
    if "Ocorreu um erro" in resultado:
        return jsonify({'error': resultado}), 500
    
    # Se os horários já foram criados, retorna status 200
    if resultado == "Os horários para o próximo mês já foram criados.":
        return jsonify({'message': resultado}), 200
    
    # Caso os registros tenham sido criados, retorna status 201
    return jsonify({'message': resultado}), 201