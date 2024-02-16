from typing import NewType, Callable

import numpy as np


def softmax_definition(X: np.array) -> np.array:
    return np.array([1/sum(np.exp(np.subtract(X, _))) for _ in np.nditer(X)])


ActivationFunction = NewType('ActivationFunction', Callable[[np.array], np.array])

sigmoid = ActivationFunction(lambda X: 1.0 / (1.0 + np.exp(-X)))
relu = ActivationFunction(lambda X: np.maximum(0, X))
softmax = ActivationFunction(softmax_definition)
linear = ActivationFunction(lambda X: X)