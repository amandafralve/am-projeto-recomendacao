import numpy as np

class PerceptronNumpy:
    def __init__(self, weights=None, bias=0.1):
        # Pesos padrão: [energy, loudness]
        default_weights = [0.8, 0.2]

        if weights is not None:
            self.weights = np.array(weights, dtype=float)
        else:
            self.weights = np.array(default_weights, dtype=float)
        
        self.bias = bias

    def _normalizar_loudness(self, loudness):
        return (loudness + 10) / 10
    
    def predict(self, energy, loudness):
        loudness_norm = self._normalizar_loudness(loudness)
        # Monta o vetor de entradas
        X = np.array([energy, loudness_norm])
        
        z = np.dot(X, self.weights) + self.bias

        preditction = 1 if z >= 0.5 else 0
    
        return {
            "prediction": preditction,
            "activation": float(z),
            "normalized_loudness": float(loudness_norm)
        }