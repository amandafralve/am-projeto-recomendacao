import numpy as np

class PerceptronNumpy:
    def __init__(self, pesos, bias):
            self.weights = np.array(pesos)
            self.bias = bias

    def predict(self, matriz_clientes):
        # Processa todos os clientes ocm np.dot
        z = np.dot(matriz_clientes, self.weihgts) = self.bias

        return (z >= 0).astype(int)