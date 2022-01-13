# Infra-PlayGround
Repo para atividades de treinamento do time de Infra


# Overview

Esse repositório contém um hello world de um back end usando Fast API (framework de Python)


## Como rodar o servidor:

### Criar o virtual enviroment de python
```py -m venv venv```
  
### Ativar o virtual enviroment
```venv\Scripts\activate```
  
### Instalar as dependências
```pip install -r requirements.txt```
  

### Comando para iniciar o servidor (porta 8000)
```uvicorn server:app --reload --host 0.0.0.0```

__OBS: importante que haja o argumento --host 0.0.0.0 para que o app seja acessível de fora do container__
  
A API já deve estar visível em [localhost:8000](http://localhost:8000/)
