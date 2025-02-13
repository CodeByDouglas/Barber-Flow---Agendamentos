# Python
from app import db
from app.models import Agendamentos

def criar_agendamento(id_funcionario: int, id_servico: int, id_horario: int, nome_cliente: str, telefone_cliente: str, admin_id: int):
    """
    Cria um agendamento no banco de dados com os parâmetros informados.
    
    Parâmetros:
      id_funcionario (int): ID do funcionário.
      id_servico (int): ID do serviço.
      id_horario (int): ID do horário.
      nome_cliente (str): Nome do cliente.
      telefone_cliente (str): Telefone do cliente.
      admin_id (int): ID do administrador.

    Retorna:
      Instância de Agendamentos ou mensagem de erro.
    """
    try:
        novo_agendamento = Agendamentos(
            id_funcionario=id_funcionario,
            id_servico=id_servico,
            id_horario=id_horario,
            nome_cliente=nome_cliente,
            telefone_cliente=telefone_cliente,
            admin_id=admin_id
        )
        db.session.add(novo_agendamento)
        db.session.commit()
        return novo_agendamento
    except Exception as e:
        db.session.rollback()
        return f"Erro ao criar agendamento: {str(e)}"