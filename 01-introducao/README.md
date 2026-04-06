### Prática
Crie um projeto simples utilizando UV e FastAPI que retorne, por meio de uma API, um exemplo de Regressão Linear implementado com scikit-learn.

#### Tecnologias utilizadas
>Python 3.14

>UV (https://docs.astral.sh/uv/)

>FastAPI

>Uvicorn

>scikit-learn

>NumPy

#### Rodar o servidor
```
uv run uvicorn main:app --reload
```

#### Testar a API
Acessar a documentação interativa (Swagger)

Abra no navegador:

http://127.0.0.1:8000/docs

Exemplo de requisição POST /predict:
```
{
  "value": 10
}
```
Resposta esperada:
```
{
  "input_value": 10,
  "predicted_value": 20
}
```