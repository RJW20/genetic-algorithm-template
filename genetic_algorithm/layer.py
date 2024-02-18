from __future__ import annotations
from typing import Callable

import numpy as np

from activation_functions import sigmoid, relu, softmax, linear, activation_by_name


class Layer:
    """Layer in a neural network."""

    def __init__(self, size: int, activation: Callable[[np.ndarray], np.ndarray]) -> None:
        self.weights = np.array([[]])
        self.bias = np.array([])
        self.activation = activation
        self.neurons = np.zeros(size)

    @property
    def size(self):
        return len(self.neurons)

    @classmethod
    def new(cls, size: int, prev_size: int, activation: Callable[[np.ndarray], np.ndarray]) -> Layer:
        """Return a newly randomized Layer.
        
        Layer parameters will have values ~U[-1,1].
        """

        layer = cls(size, activation)
        layer.weights = np.subtract(np.multiply(np.random.rand(size, prev_size), 2), 1)
        layer.bias = np.subtract(np.multiply(np.random.rand(size), 2), 1)
        
        return layer

    def propagate(self, prev_neurons: np.ndarray) -> None:
        """Compute this layer's neurons given the previous."""

        deactivated = np.add(np.dot(self.weights, prev_neurons), self.bias)
        self.neurons = self.activation(deactivated)

    def __eq__(self, other: Layer) -> bool:
        """Return True if both Layers have the same size and parameters."""

        return (np.array_equal(self.bias, other.bias) and np.array_equal(self.weights, other.weights))