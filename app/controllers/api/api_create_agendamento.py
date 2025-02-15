# Python
from flask import Blueprint, request, jsonify
from app.models import Horarios  
from app.utils.create_agendamento import criar_agendamento
from app.utils.bloc_hrs import marcar_horario_preenchido  

bp_api = Blueprint('api_create_agendamento', __name__, url_prefix='/api')

@bp_api.route('/create-agendamento', methods=['POST'])
def create_agendamento():
    data = request.get_json()
    required_keys = ['id_funcionario', 'id_servico', 'id_horario', 'nome_cliente', 'telefone_cliente']
    missing = [key for key in required_keys if key not in data]
    if missing:
        return jsonify({'error': f'Faltando parâmetros: {", ".join(missing)}'}), 400

    admin_id = data.get('admin_id')
    if not admin_id:
        return jsonify({'error': 'admin_id is required'}), 400

    # Verifica se o horário existe e não está preenchido
    horario = Horarios.query.get(data['id_horario'])
    if not horario:
        return jsonify({'error': 'Horário não encontrado.'}), 404
    if horario.preenchido:
        return jsonify({'error': 'Horário já está preenchido.'}), 400

    # Cria o agendamento
    resultado = criar_agendamento(
        id_funcionario=data['id_funcionario'],
        id_servico=data['id_servico'],
        id_horario=data['id_horario'],
        nome_cliente=data['nome_cliente'],
        telefone_cliente=data['telefone_cliente'],
        admin_id=admin_id
    )
    if isinstance(resultado, str):
        return jsonify({'error': resultado}), 500

    # Marca o horário como preenchido
    status_msg = marcar_horario_preenchido(data['id_horario'], admin_id)
    if status_msg != "Horário atualizado com sucesso.":
        return jsonify({'error': status_msg}), 500

    return jsonify({
        'message': 'Agendamento criado com sucesso.',
        'id_agendamento': resultado.id_agendamento
    }), 201