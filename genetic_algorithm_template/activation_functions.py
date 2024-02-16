import numpy as np


sigmoid = lambda X: 1.0 / (1.0 + np.exp(-X))

relu = lambda X: np.maximum(0, X)

def softmax(X: np.array) -> np.array:
    return np.array([1/sum(np.exp(np.subtract(X, _))) for _ in np.nditer(X)])

linear = lambda X: X