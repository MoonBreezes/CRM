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
    
def test_CadastrarCliente(crm, init_db):
    dadosCliente = {
        "nome": "test_user",
        "email": "test@example.com",
        "CPF_CNPJ":'780.771.820-03',
    }
    response = crm.put('/cliente/cadastrar', json=dadosCliente)
    
    data = response.get_json()
    assert "id" in data
    assert isinstance(data["id"], int)
    
    clienteCriado =  models.Cliente.query.first()
    assert clienteCriado is not None
    assert clienteCriado.nome == dadosCliente["nome"]
    assert clienteCriado.email == dadosCliente["email"] 



def test_CadastrarClienteCPFRepetido(crm, init_db):
    dadosClienteOriginal = {
        "nome": "test_user",
        "email": "test@example.com",
        "CPF_CNPJ":'780.771.820-03',
    }
    dadosClienteCPFRepetido = {
        "nome": "test_user_CPF_repetido",
        "email": "test_CPF_repetido@example.com",
        "CPF_CNPJ":'780.771.820-03',
    }
    response = crm.put('/cliente/cadastrar', json=dadosClienteOriginal)
    responseCPFRepetido = crm.put('/cliente/cadastrar', json=dadosClienteCPFRepetido)
    
    assert responseCPFRepetido.status_code == 400
    
    data = responseCPFRepetido.get_json()
    assert "message" in data
    assert data["message"]["message"] == 'Bad request: Ja existe um usario com esse CPF/CNPJ'
    assert data["message"]["success"] == False
    
    
    
    clientesCriados =  models.Cliente.query.all()
    assert clientesCriados is not None
    assert len(clientesCriados) == 1
    assert clientesCriados[0].nome == dadosClienteOriginal["nome"]
    assert clientesCriados[0].email == dadosClienteOriginal["email"] 
