from fastapi import FastAPI
from pydantic import BaseModel
from sklearn.linear_model import LinearRegression
import numpy as np
import uvicorn

app = FastAPI()

# Modelo de Regressão Linear
x = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 4, 6, 8, 10])  # relação linear: y = 2x

# Aqui é criado um objeto LinearRegression, que representa o modelo de regressão linear do scikit-learn. Só foi instanciado.
# # O método .fit() faz o treinamento do modelo usando os dados fornecidos. Aprendendo a fórmula y = 2x
model = LinearRegression()
model.fit(x, y)

# Definição do corpo da requisição (input da API); Value e o numero que queremos prever o resultado.
class PredictRequest(BaseModel):
    value: float

# Definição da resposta da API
class PredictResponse(BaseModel):
    input_value: float
    predicted_value: float
    

@app.get("/")
def root():
    return {"message": "API de Regressão Linear com FastAPI + UV + scikit-learn"}

@app.post("/predict", response_model=PredictResponse)
def predict(data: PredictRequest):
    x = np.array([[data.value]])  # Transformar o valor de entrada em um array 2D
    pred = model.predict(x)[0]  # Fazer a previsão usando o modelo treinado
    return PredictResponse(input_value=data.value, predicted_value=pred)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)