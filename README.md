# Sistema de Aluguel de Carros

Este projeto é um **Sistema de Gerenciamento de Aluguel de Carros** desenvolvido em Python, com interface gráfica (GUI) e integração com banco de dados SQLite.
O sistema permite cadastrar, editar e gerenciar carros, clientes e aluguéis de forma simples e eficiente.

## Funcionalidades
- Cadastrar carros com modelo, marca, ano, placa, categoria, combustível e transmissão
- Editar informações de carros já cadastrados
- Excluir veículos do sistema
- Listagem de carros com filtros personalizados
- Banco de dados SQLite local para persistência de dados
- Interface moderna com ttkbootstrap


## Estrutura do Projeto

```
aluguelDeCarros/
│
├── main.py                 # Arquivo principal
│
├── database/
│   ├── db.py               # Manipulação do banco de dados
│   └── __init__.py
│
├── utils/
│   ├── generator.py        # Funções auxiliares de geração
│   ├── interface.py        # Constantes e listas para formulários
│   ├── treatment.py        # Tratamento de dados
│   └── __init__.py
│
├── views/
│   ├── carRegistration.py  # Janela de cadastro e edição de carros
│   ├── mainWindow.py       # Tela principal do sistema
│   └── __init__.py
│
├── requirements.txt
├── .gitignore
├── README.md
└── rentcar.db
```

## Requisitos

Antes de executar o projeto, verifique se possui os seguintes requisitos instalados:
- Python 3.12 ou superior (testado no Python 3.14)
- Bibliotecas listadas em `requirements.txt`

Para instalar as dependências, execute:
```
pip install -r requirements.txt
```


## Como executar o projeto

#### Clonar o repoitório
```
git clone https://github.com/GabrielPaganelli/aluguelDeCarros.git
cd aluguelDeCarros
```

#### Criar o ambiente virtual
```
python -m venv .venv
```

#### Ativar o ambiente virtual
##### Windows
```
.venv\Scripts\activate
```

##### Linux/macOs
```
source .venv/bin/activate
```

#### Executar o sistema
```
python main.py
```


## Banco de Dados
O sistema usa SQLite3, e o arquivo `rentcar.db` é criado automaticamente.
<p>Caso queira resetar o banco, basta apagar esse arquivo e reiniciar o programa.