# Python
from flask import Blueprint, request, jsonify
from app.utils.create_agendamento import criar_agendamento

bp_api = Blueprint('api_create_agendamento', __name__, url_prefix='/api')

@bp_api.route('/create-agendamento', methods=['POST'])
def create_agendamento():
    data = request.get_json()
    required_keys = ['id_funcionario', 'id_servico', 'id_horario', 'nome_cliente', 'telefone_cliente']
    missing = [key for key in required_keys if key not in data]
    if missing:
        return jsonify({'error': f'Faltando parâmetros: {", ".join(missing)}'}), 400

    resultado = criar_agendamento(
        id_funcionario=data['id_funcionario'],
        id_servico=data['id_servico'],
        id_horario=data['id_horario'],
        nome_cliente=data['nome_cliente'],
        telefone_cliente=data['telefone_cliente']
    )

    if isinstance(resultado, str):
        return jsonify({'error': resultado}), 500

    return jsonify({
        'message': 'Agendamento criado com sucesso.',
        'id_agendamento': resultado.id_agendamento
    }), 201