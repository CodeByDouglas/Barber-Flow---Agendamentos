# Python
from app import db
from app.models import Horarios

def marcar_horario_preenchido(id_horario: int, admin_id: int):
    """
    Atualiza o atributo 'preenchido' para True do horário com o ID informado.

    Parâmetros:
      id_horario (int): ID do horário a ser atualizado.
      admin_id (int): ID do administrador.

    Retorna:
      Mensagem de sucesso ou erro.
    """
    horario = Horarios.query.filter_by(id_horario=id_horario, admin_id=admin_id).first()
    if not horario:
        return "Horário não encontrado."

    horario.preenchido = True
    try:
        db.session.commit()
        return "Horário atualizado com sucesso."
    except Exception as e:
        db.session.rollback()
        return f"Erro ao atualizar horário: {str(e)}"