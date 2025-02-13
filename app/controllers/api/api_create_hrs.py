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
    return jsonify({'message': resultado})