import unittest
import sys 
import os
sys.path.append(os.path.abspath('..'))
import packages.validadores as validadores

class TestValidarCPF(unittest.TestCase):
    
    def test_cpf_valido(self):
        cpfValido = '123.456.789-09'
        resultado = validadores.validarCPF(cpfValido)
        self.assertTrue(resultado)

    def test_cpf_nulo(self):
        cpfVazio = ""
        resultado = validadores.validarCPF(cpfVazio)
        self.assertFalse(resultado) 

    def test_cpf_indefinido(self):
        cpfIndefinido = None
        resultado = validadores.validarCPF(cpfIndefinido)
        self.assertTrue(resultado)  
     
    def test_cpf_invalido(self):
        cpfInvalido = '123.456.789-10'
        resultado = validadores.validarCPF(cpfInvalido)
        self.assertFalse(resultado)  

    def test_cpf_formato_sem_pontuacao(self):
        cpfFormatovalido = '12345678909'  
        resultado = validadores.validarCPF(cpfFormatovalido)
        self.assertTrue(resultado)  
        
    def test_cpf_formato_incorreto(self):
        cpfFormatoInvalido = '1234567890a'  
        resultado = validadores.validarCPF(cpfFormatoInvalido)
        self.assertFalse(resultado) 
class TestValidarCNPJ(unittest.TestCase):
    
    def test_cpf_indefinido(self):
        CNPJIndefinido = None
        resultado = validadores.validarCNPJ(CNPJIndefinido)
        self.assertTrue(resultado)

    def test_cnpj_valido(self):
        cnpj_valido = '11.222.333/0001-81'
        self.assertTrue(validadores.validarCNPJ(cnpj_valido))  
        
    def test_cnpj_formato_sem_pontuacao(self):
        cnpj_formatoInvalido = '11222333000181'
        self.assertTrue(validadores.validarCNPJ(cnpj_formatoInvalido))
    
    def test_cnpj_formato_incorreto(self):
        cnpj_formatoInvalido = '1122233300018a'
        self.assertFalse(validadores.validarCNPJ(cnpj_formatoInvalido))

    def test_cnpj_invalido(self):
        cnpj_invalido = '11.222.343/0001-81'
        self.assertFalse(validadores.validarCNPJ(cnpj_invalido))

    def test_cnpj_nulo(self):
        cnpj_nulo = ""
        self.assertFalse(validadores.validarCNPJ(cnpj_nulo))
    


class TestValidarCEP(unittest.TestCase):
    def test_cep_indefinido(self):
        cepIndefinido = None
        self.assertTrue(validadores.validarCEP(cepIndefinido)) 

    def test_cep_nulo(self):
        cepNulo = ""
        self.assertFalse(validadores.validarCEP(cepNulo))
    
    def test_cep_valido(self):
        cep_valido = '12.345-678'
        self.assertTrue(validadores.validarCEP(cep_valido))  

    def test_cep_invalido(self):
        cep_invalido = '12345678'
        self.assertFalse(validadores.validarCEP(cep_invalido))  

class TestValidarTelefoneFixo(unittest.TestCase):
    def test_telefone_valido(self):
        telefone_indefinido = None
        self.assertTrue(validadores.validarTelefoneFixo(telefone_indefinido))

    def test_telefone_valido(self):
        telefone_valido = '(12) 3456-7890'
        self.assertTrue(validadores.validarTelefoneFixo(telefone_valido))  

    def test_telefone_invalido(self):
        telefone_invalido = '(12) 3456-78901'
        self.assertFalse(validadores.validarTelefoneFixo(telefone_invalido))

    def test_telefone_nulo(self):
        telefone_nulo = ""
        self.assertFalse(validadores.validarTelefoneFixo(telefone_nulo))    
    
    def test_telefone_ddd_invalido(self):
        ddd_invalido = '(36) 3456-7890'
        self.assertFalse(validadores.validarTelefoneFixo(ddd_invalido))

    def test_telefone_celular_valido(self):
        celular_valido = '(31)8888-8888'
        self.assertFalse(validadores.validarTelefoneFixo(celular_valido))

class TestValidarCelular(unittest.TestCase):
    def test_validar_celular_indefinido(self):
        celular_indefinido = None
        self.assertTrue(validadores.validarCelular(celular_indefinido))

    def test_celular_oito_digitos_valido(self):
        celular_valido = '(31) 9123-4567'
        self.assertTrue(validadores.validarCelular(celular_valido))  

    
    def test_celular_oito_digitos_invalido(self):
        celular_invalido = '(31) 9123-a567'
        self.assertFalse(validadores.validarCelular(celular_invalido))  
    
    
    def test_celular_nove_digitos_valido(self):
        celular_valido = '(21) 91234-5678'
        self.assertTrue(validadores.validarCelular(celular_valido))  

    def test_celular_nove_digitos_invalido(self):
        celular_invalido = '(31) 912 34-567 89'
        self.assertFalse(validadores.validarCelular(celular_invalido)) 

    def test_celular_nulo(self):
        celular_nulo = ""
        self.assertFalse(validadores.validarCelular(celular_nulo))     

class TestValidarEmail(unittest.TestCase):
    def test_validar_Email_Indefinido(self):
        email_indefinido = None
        self.assertTrue(validadores.validarEmail(email_indefinido))
    
    def test_email_valido(self):
        email_valido = 'exemplo@example.com.br'
        self.assertTrue(validadores.validarEmail(email_valido))  

    def test_email_invalido(self):
        email_invalido = 'exemploexample.com'
        self.assertFalse(validadores.validarEmail(email_invalido))

    def test_email_invalido_multiplos_arrobas(self):
        email_multiplos_arrobas = 'abc@def@xyz.com'
        self.assertFalse(validadores.validarEmail(email_multiplos_arrobas))

    def test_email_nulo(self):
        email_nulo = ""
        self.assertFalse(validadores.validarEmail(email_nulo))            

class TestValidarEstado(unittest.TestCase):
    def test_estado_valido(self):
        estado_valido = 'MG'
        self.assertTrue(validadores.validarSiglaUF(estado_valido))  

    
    def test_estado_indefinido(self):
        estado_indefinido = None
        self.assertFalse(validadores.validarSiglaUF(estado_indefinido)) 

    def test_estado_invalido(self):
        estado_invalido = 'ZZ'
        self.assertFalse(validadores.validarSiglaUF(estado_invalido))

    def test_estado_nulo(self):
        estado_nulo = ""
        self.assertFalse(validadores.validarSiglaUF(estado_nulo))    

class TestValidarNumero(unittest.TestCase):
    def test_numero_valido(self):
        numero_valido = '208'
        self.assertTrue(validadores.validarNumero(numero_valido))  

    def test_numero_nulo(self):
        numero_nulo = ""
        self.assertFalse(validadores.validarNumero(numero_nulo))

    
    def test_numero_indefinido(self):
        numero_indefinido = None
        self.assertFalse(validadores.validarNumero(numero_indefinido))  

    def test_numero_invalido(self):
        numero_invalido = 'abcde'
        self.assertFalse(validadores.validarNumero(numero_invalido)) 

    def test_numero_invalido_misto(self):
        numero_invalido_misto = '1ab2cd3e'
        self.assertFalse(validadores.validarNumero(numero_invalido_misto))         

class Testdata(unittest.TestCase):
    def test_dataValida(self):
        dataValida = '2023-08-01'
        self.assertTrue(validadores.validarData(dataValida))  

    def test_data_indefinida(self):
        dataIndefinida = None
        self.assertTrue(validadores.validarData(dataIndefinida))

    def test_data_nula(self):
        dataNula = ""
        self.assertFalse(validadores.validarData(dataNula))
        
class TestSiglasUF(unittest.TestCase):
    def test_SiglaVazia(self):
        siglaVazia = None
        self.assertFalse(validadores.validarSiglaUF(siglaVazia))  

    def test_SiglaEmbraco(self):
        siglaVazia = ""
        self.assertFalse(validadores.validarSiglaUF(siglaVazia))
        
    def test_SiglaApenasEspacoesEmbranco(self):
        siglaApenasEspacoesEmbranco = " "
        self.assertFalse(validadores.validarSiglaUF(siglaApenasEspacoesEmbranco))

    def test_SiglaInvalida(self):
        siglaInvalida = "GM"
        self.assertFalse(validadores.validarSiglaUF(siglaInvalida))
    
    def test_SiglaMinuscula(self):
        siglaMinuscula = "mg"
        self.assertFalse(validadores.validarSiglaUF(siglaMinuscula))

    def test_SiglaValida(self):
        siglaValida = "MG"
        self.assertTrue(validadores.validarSiglaUF(siglaValida))     


if __name__ == '__main__':
    unittest.main()