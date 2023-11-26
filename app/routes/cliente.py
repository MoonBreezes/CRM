from app import db
from app import models
from app.serializers import ClienteSchema
from datetime import datetime
from flask import Blueprint, jsonify, request,abort
from json import dumps as jsondump
import json
import packages.validadores as validadores
import app.response as response
import app.pipelineValidacoes as pipelineValidacoes
import app.bodyParameter  as bodyParameter
import app.alterarAtributoBd as alterarAtributoBd
import app.pyDateTime as pyDateTime
from flask_restx import Api, Namespace, Resource, fields
from datetime import datetime


cliente = Blueprint('cliente', __name__)


nsCliente = Namespace("cliente",  description="Operação Com Clientes")

cliente_model = nsCliente.model('Cliente', {
    'CPF_CNPJ': fields.String(required=False, description="identificador de Cliente PF ou PJ"),
    'nome': fields.String(required=False, description="Nome cliente"),
    'email': fields.String(required=False, description="endereco de email"),
    'telefone': fields.String(required=False,description="telefone"),
    'whatsapp': fields.String(required=False,description="whatsapp para contato"),
    'celular': fields.String(required=False,description="User's name"),
    'dataNascimento': fields.String(required=False,description="User's name"),
})


# ROTAS 
@nsCliente.route('/cadastrar', methods=['PUT'])
class ClienteResource(Resource):
    @nsCliente.expect(cliente_model, validate=True)
    def put(self):
        return cadastrarCliente()
    
@nsCliente.route("/listarTodos",methods=['GET'])
class ClienteResource(Resource):
    def get(self):
        return listarTodosClientes()
    
@nsCliente.route('/listarPessoaJuridica',methods=['GET'])
class ClientePJResource(Resource):
    def get(self):
        return listarPessoaJuridica()

@nsCliente.route('/listarPessoaFisica', methods=['GET'])
class ClientePFResource(Resource):
    def get(self):
        return listarPessoaFisica()
    
@nsCliente.route('/<id>/atualizar', methods=['PATCH'])
class ClienteResource(Resource):
    @nsCliente.expect(cliente_model, validate=True)
    def patch(self,id):
        return atualizarCadastroCliente(id)
    
# @nsCliente.route('/<id>/apagarAtributo/<nomeAtributo>', methods=['DELETE'])
# class ClienteResource(Resource):
#     def delete(self,id):
#         return apagarAtributo(id)
    
  
@nsCliente.route('/<id>/deletar', methods=['DELETE'])
class ClienteResource(Resource):
    def delete(self,id):
        return deletarCliente(id)
    

#Funcoes

def cadastrarCliente():
    response_data = json.loads(request.data.decode())
    CPF_CNPJ = bodyParameter.get(response_data,'cpf_cnpj')
    nome = bodyParameter.get(response_data,'nome')
    email = bodyParameter.get(response_data,'email')
    telefone = bodyParameter.get(response_data,'telefone')
    whatsapp = bodyParameter.get(response_data,'whatsapp')
    celular = bodyParameter.get(response_data,'celular')
    dataNascimento = bodyParameter.get(response_data,'dataNascimento')
    
    resultado,mensagem = pipelineValidacoes.Executar(
        [
            ('nome' in response_data,"Para cadastrar um cliente é preciso de um nome"),
            (validadores.validarCPF_CNPJ(CPF_CNPJ), "CPF ou CNPJ invalido."),
            (validadores.validarEmail(email), "Email Invalido"),
            (validadores.validarTelefoneFixo(telefone), "Telefone Fixo Invalido"),
            (validadores.validarData(dataNascimento), "Data de nascimento Invalida"),
            (validadores.validarCelular(celular), "Celular Invalido"),
            ( models.Cliente.query.filter_by(CPF_CNPJ=CPF_CNPJ).first() is None,"Ja existe um usario com esse CPF/CNPJ" )
        ]
    )
    
    if resultado is False: 
        codigo, mensagem = response.bad_request(mensagem)
        abort(codigo, mensagem)

    cliente_obj = models.Cliente(
        CPF_CNPJ = CPF_CNPJ,
        nome = nome,
        email = email,
        telefone = telefone,
        whatsapp = whatsapp,
        celular = celular,
        dataNascimento =  datetime.strptime(dataNascimento, "%Y-%m-%d") if dataNascimento is not None else None
    )

    db.session.add(cliente_obj)

    db.session.commit()
    
    return {'id':cliente_obj.id}

def listarPessoaFisica():
    result = models.Cliente.query.filter(models.Cliente.CPF_CNPJ.ilike('___.___.___-__')).filter_by(dataExclusao=None).all()
    return ClienteSchema(many=True).jsonify(result)

def listarPessoaJuridica():
    result = models.Cliente.query.filter(models.Cliente.CPF_CNPJ.ilike('__.___.___/____-__')).filter_by(dataExclusao=None).all()
    return ClienteSchema(many=True).jsonify(result)

def listarTodosClientes():
    result = models.Cliente.query.filter_by(dataExclusao=None).all()
    return ClienteSchema(many=True).jsonify(result)

def atualizarCadastroCliente(id):
    response_data = json.loads(request.data.decode())
    
    CPF_CNPJ = bodyParameter.get(response_data,'CPF_CNPJ')
    print("CPF_CNPJ",CPF_CNPJ)
    nome = bodyParameter.get(response_data,'nome')
    email = bodyParameter.get(response_data,'email')
    telefone = bodyParameter.get(response_data,'telefone')
    whatsapp = bodyParameter.get(response_data,'whatsapp')
    celular = bodyParameter.get(response_data,'celular')
    dataNascimento = bodyParameter.get(response_data,'dataNascimento')
    
    
    resultado,mensagem = pipelineValidacoes.Executar(
        [
            (validadores.validarCPF_CNPJ(CPF_CNPJ), "CPF ou CNPJ invalido."),
            (validadores.validarEmail(email), "Email Invalido"),
            (validadores.validarTelefoneFixo(telefone), "Telefone Fixo Invalido"),
            (validadores.validarData(dataNascimento), "Data de nascimento Invalida"),
            (validadores.validarCelular(celular), "Celular Invalido"),
        ]
    )
    if resultado is False: 
        codigo, mensagem =  response.bad_request(mensagem)
        abort(codigo, mensagem)
        
    cliente_obj = models.Cliente.query.filter_by(id=id).filter_by(dataExclusao=None).first()
    if cliente_obj is None:
        codigo, mensagem =  response.bad_request("Cliente Nao Encontrado")
        abort(codigo, mensagem)


    alterarAtributoBd._(cliente_obj, 'nome', nome)
    alterarAtributoBd._(cliente_obj, 'email', email)
    alterarAtributoBd._(cliente_obj, 'whatsapp', whatsapp)
    alterarAtributoBd._(cliente_obj, 'dataNascimento',  pyDateTime.converter_AAAA_MM_DD(dataNascimento))
    print("CPF_CNPJ",CPF_CNPJ)
    alterarAtributoBd._(cliente_obj, 'CPF_CNPJ', CPF_CNPJ)

    db.session.commit()
    
    return True


def deletarCliente(id):
    cliente_obj = models.Cliente.query.filter_by(id=id).first()
    if cliente_obj is None:
        codigo, mensagem = response.bad_request("Cliente Nao Encontrado")
        abort(codigo, mensagem)
    dataExclusao =  datetime.now()
    setattr(cliente_obj, 'dataExclusao', dataExclusao)
    db.session.commit()
    return True
    