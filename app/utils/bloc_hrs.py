# Python
from app import db
from app.models import Horarios

def marcar_horario_preenchido(id_horario: int):
    """
    Atualiza o atributo 'preenchido' para True do horário com o ID informado.

    Parâmetros:
      id_horario (int): ID do horário a ser atualizado.

    Retorna:
      Mensagem de sucesso ou erro.
    """
    horario = Horarios.query.get(id_horario)
    if not horario:
        return "Horário não encontrado."

    horario.preenchido = True
    try:
        db.session.commit()
        return "Horário atualizado com sucesso."
    except Exception as e:
        db.session.rollback()
        return f"Erro ao atualizar horário: {str(e)}"