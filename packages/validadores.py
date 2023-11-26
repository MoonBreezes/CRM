import re
from datetime import datetime
import validate_docbr
from validate_email_address import validate_email

def validarCPF(strCpf:str) -> bool:
    if strCpf is None:
      return True
    if strCpf=='': 
      return False
    validador = validate_docbr.CPF()
    return  validador.validate(strCpf)

def validarCNPJ(strCnpj:str) -> bool:
  if(strCnpj is None):
    return True
  if strCnpj == '': 
      return False
  
  validador = validate_docbr.CNPJ()
  return  validador.validate(strCnpj)

def validarCPF_CNPJ(cpfCnpj:str) -> bool:
  return validarCPF(cpfCnpj) or validarCNPJ(cpfCnpj)

def validarEmail(email:str) -> bool:
  if(email==None):
    return True
  if email == '': 
      return False
  return validate_email(email)

def validarCelular(celular:str) -> bool:
  if(celular==None):
    return True
  if celular == '': 
      return False
  padrao = r'\(\d{2}\) (9\d{4}-\d{4}|\d{4}-\d{4})'  # padrão regex para '(XX) 9XXXX-XXXX' ou '(XX) XXXX-XXXX'

  if re.match(padrao, celular):
      return True
  else:
      return False



def validarTelefoneFixo(telefoneFixo: str) -> bool:
  if(telefoneFixo==None):
    return True
  if telefoneFixo == '': 
      return False
  telefoneFixo = telefoneFixo.replace('+', '')
  telefoneFixo = telefoneFixo.replace('(', '')
  telefoneFixo = telefoneFixo.replace(')', '')
  telefoneFixo = telefoneFixo.replace('-', '')
  telefoneFixo = telefoneFixo.replace(' ', '')
  telefoneFixo = telefoneFixo.removeprefix('0')

  size = len(telefoneFixo)
  
  ddds = re.compile("(1[1-9]|2[12478]|3[1-578])|4[1-9]|5[13-5]|6[1-9]|7[13-579]|8[1-9]|9[1-9]")
  valid_ddd = ddds.match(telefoneFixo)
  if(not valid_ddd):
    return False
  
  if(size!=10):
    return False

  valid_prefixes = ['2','3','4','5']
  if(telefoneFixo[-8] not in valid_prefixes):
    return False
  
  return True

def validarCEP(cep: str) -> bool:
  if(cep==None):
    return True
  
  cep_standard = re.compile("[0-9]{2}[.][0-9]{3}[-][0-9]{3}$")
  legal_format = cep_standard.match(cep)
  if(not legal_format):
    return False
  return True

def validarCodigoBarras(codigoBarras: str) -> bool:
  return True 

def validarData(data: str) -> bool:
  if data == None: 
      return True
  if data == '': 
      return False
  formato = "%Y-%m-%d"
  try:
      datetime.strptime(data, formato)
      return True
  except ValueError:
      return False
  
def validarSiglaUF(estado: str) -> bool:
  if estado is None:
    return False
  estados = {'AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO'}
  return estado in estados

def validarNumero(numero: str) -> bool:
  if numero is None:
    return False
  return numero.isnumeric()
