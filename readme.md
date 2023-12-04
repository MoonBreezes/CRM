[![GitHub Actions (Tests)](https://github.com/MoonBreezes/CRM/actions/workflows/tests.yml/badge.svg)](https://github.com/MoonBreezes/CRM/actions/workflows/tests.yml) 
[![codecov](https://codecov.io/gh/MoonBreezes/CRM/settings/branch/master/graph/badge.svg?token=P7FUEKQZ8L)](https://codecov.io/gh/MoonBreezes/CRM/settings)

# Sistema de controle de acesso com Interface Web e API REST
### 1. Nomes dos membros do grupo:

* Lecio Alves
* Matheus Schimieguel Silva

### 2. Explicação do sistema:

O sistema é  uma API Rest com um banco de dados para um sistema simples de CRM (customer relationship management).Composto com tarefas simples como cadastrar um cliente , um produto e deleta-los respectivamente. 

### 3. Explicação das tecnologias utilizadas.

* Python 3.11 - Linguagem de programação
* Python pip - Gerenciador de pacotes da linguagem Python
* Python 3 Virtual Environment - Ambiente virtual para isolar pacotes instalados pelo Python pip
* Python Flask - Framework em Python para desenvolvimento de sistemas web
* Python Flask-restx (swagger) - Pacote em Python para documentar APIs REST em flask com um interface gráfica swagger
* SQLAlchemy - Framework em Python que implementa banco de dados com interface ORM (Object Relational Mapping)


## Desenvolvimento no Linux (Debian 9 64 Bit) e e Windows 10:
### Dependências:
* Desenvolvido no Debian 9 64-bit e Windows 10 
* Python 3.11
* Python pip
* Python 3 Virtual Environment


```bash
sudo apt install python3 python3-venv python3-pip
```

### Configurando o ambiente:
1. Criação:    `python3 -m venv ./venv`
2. Ativalção:  `source venv/bin/activate`
3. Dependências do sistema: `pip install -r requirements.txt`

### Executando:
1. Ativando ambiente:  `source venv/bin/activate`
2. Executando: 
    * no linux: 
    `.\run.sh`
    * no Windows: 
    `.\run.ps1`

3. Desativando ambiente: `deactivate`
