from flask import Blueprint, jsonify
from app.utils.create_hrs import gerar_horarios_proximo_mes


bp_api = Blueprint('api_create_hrs', __name__, url_prefix='/api')

@bp_api.route('/create-hrs', methods=['GET'])
def create_hrs():
  
    resultado = gerar_horarios_proximo_mes()
    return jsonify({'message': resultado})