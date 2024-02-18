from typing import Callable, Literal

import numpy as np


sigmoid = lambda X: 1.0 / (1.0 + np.exp(-X))

relu = lambda X: np.maximum(0, X)

def softmax(X: np.ndarray) -> np.ndarray:
    return np.array([1/sum(np.exp(np.subtract(X, _))) for _ in np.nditer(X)])

linear = lambda X: X

def activation_by_name(name: Literal['sigmoid', 'relu', 'softmax', 'linear']) -> Callable[[np.ndarray], np.ndarray]:
    """Return activation function from name."""

    activations = {
        'sigmoid': sigmoid,
        'relu': relu,
        'softmax': softmax,
        'linear': linear,
    }

    try:
        activation = activations[name]
    except KeyError:
        raise TypeError

    return activation