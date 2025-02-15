# Python
import pytest
from datetime import date, time
from app import create_app, db
from app.models import Administrador, Funcionarios, Horarios

@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    # Use SQLite in-memory database for testing
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite://"
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            # Cria um Administrador
            admin = Administrador(email="admin@example.com", senha="senha", nome_barbearia="Barbearia Teste")
            db.session.add(admin)
            db.session.commit()
            # Cria um Funcionário
            funcionario = Funcionarios(nome="Funcionario Teste", admin_id=admin.id_administrador)
            db.session.add(funcionario)
            db.session.commit()
            # Cria um Horário para o dia 20/10/2023
            horario_entry = Horarios(
                data=date(2023, 10, 20),
                horario=time(10, 0),
                preenchido=False,
                id_funcionario=funcionario.id_funcionario,
                admin_id=admin.id_administrador
            )
            db.session.add(horario_entry)
            db.session.commit()
        yield client
        with app.app_context():
            db.drop_all()

def test_consulta_hrs_missing_params(client):
    # Testa quando parâmetros estão faltando na requisição
    response = client.post("/api/consulta_hrs", json={"id": 1})
    assert response.status_code == 400
    data = response.get_json()
    assert 'erro' in data.get('error').lower()

def test_consulta_hrs_no_results(client):
    # Testa consulta onde nenhum horário é encontrado
    payload = {
        "id": 1,
        "dia": 15,
        "mes": 10,
        "ano": 2023,
        "admin_id": 1
    }
    response = client.post("/api/consulta_hrs", json=payload)
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) == 0

def test_consulta_hrs_success(client):
    # Consulta para um horário que foi criado (20/10/2023)
    payload = {
        "id": 1,
        "dia": 20,
        "mes": 10,
        "ano": 2023,
        "admin_id": 1
    }
    response = client.post("/api/consulta_hrs", json=payload)
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) == 1
    horario = data[0]
    assert horario.get("id_funcionario") == 1
    assert horario.get("data") == "20/10/2023"