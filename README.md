O que foi usado:
Visual Studio Code 1.101.0
python 3.10
fastapi 0.115.12
uvicorn 0.34.2
pydantic 2.11.4
pydantic-settings 2.9.1
motor 3.3.1
pytest = 7.4.3
pytest-asyncio 0.21.1
pre-commit 3.5.0
pyenv 3.12.1
poetry 1.8.4

Para os códigos que criei funcione, siga o modo de uso abaixo:
Criar a pasta para colocar o projeto
Abrir a pasta criada com Visual Studio Code
No terminal digitar: poetry config virtualenvs.in-project true (Aqui está dizendo para o poetry, tomar conta do ambiente virtual)
Agora vamos criar o projeto com o comando:  poetry new TDD_Project (Esse comando cria o projeto pré configurado, e o "TDD_Project" é o nome do projeto)
Entre na pasta do projeto criado, que no nosso caso é o TDD_project
Agora use o comando: pyenv local 3.12.1 (Para o pyenv, ficar responsável por essa versão)
Usar o comando: poetry env use 3.12.1 (Para dizer que eu quero o Python 3.12.1)
Colocar dentro desse arquivo: pyproject.toml (colar essas dependências: fastapi = "^0.115.12"
uvicorn = "^0.34.2"
pydantic = "^2.11.4"
pydantic-settings = "^2.9.1"
motor = "^3.3.1"
pytest = "^7.4.3"
pytest-asyncio = "^0.21.1"
pre-commit = "^3.5.0" , abaixo de onde está: [tool.poetry.dependencies] )
No terminal use o comando: poetry shell
Agora use o comando: poetry install
