O que foi usado: </br>
Visual Studio Code 1.101.0</br>
python 3.10</br>
fastapi 0.115.12</br>
uvicorn 0.34.2</br>
pydantic 2.11.4</br>
pydantic-settings 2.9.1</br>
motor 3.3.1</br>
pytest = 7.4.3</br>
pytest-asyncio 0.21.1</br>
pre-commit 3.5.0</br>
pyenv 3.12.1</br>
poetry 1.8.4</br>

Para os códigos que criei funcione, siga o modo de uso abaixo:</br>
Criar a pasta para colocar o projeto</br>
Abrir a pasta criada com Visual Studio Code</br>
No terminal digitar: poetry config virtualenvs.in-project true (Aqui está dizendo para o poetry, tomar conta do ambiente virtual)</br>
Agora vamos criar o projeto com o comando:  poetry new TDD_Project (Esse comando cria o projeto pré configurado, e o "TDD_Project" é o nome do projeto)</br>
Entre na pasta do projeto criado, que no nosso caso é o TDD_project</br>
Agora use o comando: pyenv local 3.12.1 (Para o pyenv, ficar responsável por essa versão)</br>
Usar o comando: poetry env use 3.12.1 (Para dizer que eu quero o Python 3.12.1)</br>
Colocar dentro desse arquivo: pyproject.toml (colar essas dependências: fastapi = "^0.115.12"</br>
uvicorn = "^0.34.2"</br>
pydantic = "^2.11.4"</br>
pydantic-settings = "^2.9.1"</br>
motor = "^3.3.1"</br>
pytest = "^7.4.3"</br>
pytest-asyncio = "^0.21.1"</br>
pre-commit = "^3.5.0" , abaixo de onde está: [tool.poetry.dependencies] )</br>
No terminal use o comando: poetry shell</br>
Agora use o comando: poetry install</br>
