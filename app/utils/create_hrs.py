import calendar
from app import db
from datetime import datetime, time, date
from app.models import Horarios, Funcionarios

def gerar_horarios_proximo_mes():
    # Verifica se hoje é o primeiro dia do mês
    
    hoje = datetime.today()
    if hoje.day != 1:
        return "Hoje não é o primeiro dia do mês. Nenhum horário foi gerado."

    # Determina o próximo mês e o ano correspondente
    if hoje.month == 12:  # se for dezembro, próximo mês é janeiro do próximo ano
        mes_proximo = 1
        ano_proximo = hoje.year + 1
    else:
        mes_proximo = hoje.month + 1
        ano_proximo = hoje.year

    # Obtem a quantidade de dias do próximo mês
    _, total_dias = calendar.monthrange(ano_proximo, mes_proximo)

    # Data inicial e final do próximo mês para a verificação
    data_inicial = date(ano_proximo, mes_proximo, 1)
    data_final = date(ano_proximo, mes_proximo, total_dias)

    # Verifica se já existem horários criados para o próximo mês
    horarios_existentes = Horarios.query.filter(
        Horarios.data >= data_inicial,
        Horarios.data <= data_final
    ).first()
    if horarios_existentes:
        return "Os horários para o próximo mês já foram criados."

    total_registros = 0
    log_detalhado = []

    try:
        # Busca todos os funcionários (barbeiros) disponíveis no sistema
        funcionarios = Funcionarios.query.all()
        
        # Itera sobre cada dia do próximo mês
        for dia in range(1, total_dias + 1):
            data_registro = date(ano_proximo, mes_proximo, dia)
            # Cria registrjos para cada horário de 8h até 18h (inclusive)
            for hora in range(8, 19): 
                horario_registro = time(hora, 0)
                # Cria um registro para cada funcionário
                for funcionario in funcionarios:
                    registro = Horarios(
                        data=data_registro,
                        horario=horario_registro,
                        preenchido=False,
                        id_funcionario=funcionario.id_funcionario
                    )
                    db.session.add(registro)
                    total_registros += 1
                    log_detalhado.append(
                        f"{data_registro} {horario_registro} - id_funcionario: {funcionario.id_funcionario}"
                    )
        
        # Tenta confirmar as inserções no banco de dados
        db.session.commit()
    
    except Exception as e:
        db.session.rollback()
        return f"Ocorreu um erro ao inserir os registros: {str(e)}"
    
    return f"Total de registros criados: {total_registros}. Detalhes: " + "; ".join(log_detalhado)