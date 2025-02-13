# Python
from datetime import date
from app.models import Horarios

def consultar_horarios(id_funcionario: int, dia: int, mes: int, ano: int, admin_id: int):
    """Retorna uma lista de dicionários com os horários e sua disponibilidade."""
    data_consulta = date(ano, mes, dia)
    horarios = Horarios.query.filter(
        Horarios.id_funcionario == id_funcionario,
        Horarios.data == data_consulta,
        Horarios.admin_id == admin_id
    ).all()
    
    resultado = []
    for h in horarios:
        resultado.append({
            "id": h.id_horario,
            "id_funcionario": h.id_funcionario,
            "data": h.data.strftime("%d/%m/%Y") if h.data else None,
            "horario": h.horario.strftime("%H:%M:%S") if h.horario else None,
            "preenchido": h.preenchido
        })
    return resultado