from typing import Callable

import numpy as np


sigmoid = lambda X: 1.0 / (1.0 + np.exp(-X))

relu = lambda X: np.maximum(0, X)

def softmax(X: np.array) -> np.array:
    return np.array([1/sum(np.exp(np.subtract(X, _))) for _ in np.nditer(X)])

linear = lambda X: X


def activation_by_name(name: str) -> Callable[[np.array], np.array]:
    """Return activation function from name."""

    activations = [('sigmoid', sigmoid), ('relu', relu), ('softmax', softmax), ('linear', linear)]
    func = [activation[1] for activation in activations if activation[0].lower() == name.lower()]
    assert len(func) == 1, f"invalid activation function {name}"

    return func[0]