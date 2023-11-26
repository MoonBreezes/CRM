# test_app.py

import pytest
import sys
import os
print()

sys.path.append(os.getcwd())

from app import create_app, db,models

@pytest.fixture
def app():
    app = create_app("testing")
    return app

@pytest.fixture
def crm(app):
    return app.test_client()

@pytest.fixture
def init_db(app):
    with app.app_context():
        db.create_all()
        yield db  
        db.session.remove()
        db.drop_all()

def test_ListarTodosClientes_BancoComNenhumCliente(crm, init_db):

    response = crm.get('/cliente/listarTodos')

    data = response.get_json()

    assert response.status_code == 200
    assert len(data) == 0  
    print(data)


def test_ListarTodosClientes_BancoComUmCliente(crm, init_db):
    cliente = models.Cliente(CPF_CNPJ='780.771.820-03',nome='test_user', email='test@example.com')
    init_db.session.add(cliente)
    init_db.session.commit()

    response = crm.get('/cliente/listarTodos')

  
    data = response.get_json()

    assert response.status_code == 200
    assert len(data) == 1  
    assert data[0]['nome'] == 'test_user'
    assert data[0]['email'] == 'test@example.com'

def test_ListarTodosClientes_BancoComVariosClientes(crm, init_db):
    for i in range(10):
        cliente = models.Cliente(nome='test_user'+str(i), email='test@example.com')
        init_db.session.add(cliente)
        init_db.session.commit()

    response = crm.get('/cliente/listarTodos')

  
    data = response.get_json()

    assert response.status_code == 200
    assert len(data) == 10 
    assert data[0]['nome'] == 'test_user0'
    assert data[0]['email'] == 'test@example.com'