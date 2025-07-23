Este projeto foi desenvolvido para, ampliar meu conhecimento de Desenvolvimento Orientado a Teste, mais conhecido como TDD.

O que foi usado:
Visual Studio Code 1.101.0
python 3.10
fastapi 0.115.12
uvicorn 0.34.2
pydantic 2.11.7
pydantic-settings 2.9.1
motor 3.3.1
pytest = 7.4.3
pytest-asyncio 0.21.1
pre-commit 3.5.0
pyenv 3.12.1
poetry 1.8.4

Para configurar o ambiente e os códigos funcione perfeitamente, siga o modo de uso abaixo:
1. Criar a pasta para colocar o projeto
2. Abrir a pasta criada com Visual Studio Code
3. No terminal, digitar: poetry config virtualenvs.in-project true (Aqui está dizendo para o poetry, tomar conta do ambiente virtual)
4. Agora vamos criar o projeto com o comando:  poetry new TDD_Project (Esse comando cria o projeto pré configurado, e o "TDD_Project" é o nome do projeto)
5. Entre na pasta do projeto criado, que no nosso caso é o TDD_project
6. Agora use o comando: pyenv local 3.12.1 (Para o pyenv, ficar responsável por essa versão)
7. Usar o comando: poetry env use 3.12.1 (Para dizer que eu quero o Python 3.12.1)
8. Colocar dentro desse arquivo: pyproject.toml (colar essas dependências:
fastapi = "^0.115.12"
uvicorn = "^0.34.2"
pydantic = "^2.5.1"
pydantic-settings = "^2.9.1"
motor = "^3.3.1"
pytest = "^8.4.0"
pytest-asyncio = "^0.21.1"
pre-commit = "^4.2.0" , abaixo de onde está: [tool.poetry.dependencies] )
9. No terminal use o comando: poetry shell
10. Agora use o comando: poetry install

Obs: toda vez que for rodar o código, mesmo com a configuração acima, tem que usar esses três comandos:
pyenv local 3.12.1
poetry env use 3.12.1
poetry shell
