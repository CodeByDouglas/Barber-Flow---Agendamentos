from flask import Blueprint, request, jsonify
from app.utils.create_hrs import gerar_horarios_proximo_mes
import calendar
from app import db
from datetime import datetime, time, date
from app.models import Horarios, Funcionarios

def gerar_horarios_proximo_mes(admin_id):
    hoje = datetime.today()

    # Determina o próximo mês e o ano correspondente
    if hoje.month == 12:
        mes_proximo = 1
        ano_proximo = hoje.year + 1
    else:
        mes_proximo = hoje.month + 1
        ano_proximo = hoje.year

    _, total_dias = calendar.monthrange(ano_proximo, mes_proximo)
    data_inicial = date(ano_proximo, mes_proximo, 1)
    data_final = date(ano_proximo, mes_proximo, total_dias)

    total_registros = 0
    log_detalhado = []

    # Busca todos os funcionários relacionados ao admin_id
    funcionarios = Funcionarios.query.filter_by(admin_id=admin_id).all()

    for funcionario in funcionarios:
        # Verifica se já existem horários criados para esse funcionário no próximo mês
        horarios_existentes = Horarios.query.filter(
            Horarios.id_funcionario == funcionario.id_funcionario,
            Horarios.data >= data_inicial,
            Horarios.data <= data_final
        ).first()

        # Se já existir, pula a criação para esse funcionário
        if horarios_existentes:
            continue

        # Caso contrário, cria os horários para cada dia e hora desejada
        for dia in range(1, total_dias + 1):
            data_registro = date(ano_proximo, mes_proximo, dia)
            for hora in range(8, 19): 
                horario_registro = time(hora, 0)
                registro = Horarios(
                    data=data_registro,
                    horario=horario_registro,
                    preenchido=False,
                    id_funcionario=funcionario.id_funcionario,
                    admin_id=admin_id
                )
                db.session.add(registro)
                total_registros += 1
                log_detalhado.append(
                    f"{data_registro} {horario_registro} - id_funcionario: {funcionario.id_funcionario}"
                )

    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return f"Ocorreu um erro ao inserir os registros: {str(e)}"

    if total_registros == 0:
        return "Os horários para o próximo mês já foram criados para todos os funcionários."
    
    return f"Total de registros criados: {total_registros}. Detalhes: " + "; ".join(log_detalhado)


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