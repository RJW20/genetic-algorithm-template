from __future__ import annotations
from typing import Callable

import numpy as np

from activation_functions import sigmoid, relu, softmax, linear, activation_by_name


class Layer:
    """Layer in a neural network."""

    __slots__ = (
        "size",
        "weights",
        "bias",
        "activation",
        "neurons",
    )

    def __init__(self, size: int, activation: Callable[[np.array], np.array]) -> None:
        self.size = size
        self.activation = activation
        self.neurons = np.zeros(size)

    @classmethod
    def new(cls, size: int, prev_size: int, activation: Callable[[np.array], np.array]) -> Layer:
        """Return a newly randomized Layer.
        
        Layer parameters will have values ~U[-1,1].
        """

        layer = cls(size, activation)
        layer.weights = np.subtract(np.multiply(np.random.rand(size, prev_size), 2), 1)
        layer.bias = np.subtract(np.multiply(np.random.rand(size), 2), 1)
        
        return layer

    def propagate(self, prev_neurons: np.array) -> None:
        """Compute this layer's neurons given the previous."""

        deactivated = np.add(np.dot(self.weights, prev_neurons), self.bias)
        self.neurons = self.activation(deactivated)

    def __eq__(self, other: Layer) -> bool:
        """Return True if both Layers have the same size and parameters."""

        if not np.array_equal(self.bias, other.bias): return False      #most of the time we will know by now
        if not np.array_equal(self.weights, other.weights): return False
        return True
    
    def __getstate__(self) -> dict:
        """Return a dictionary of attributes and their values as (key, value) pairs."""

        d = dict()
        d['size'] = self.size
        d['weights'] = self.weights
        d['bias'] = self.bias
        d['activation'] = str(self.activation)
        d['neurons'] = self.neurons

        return d
    
    def __setstate__(self, d: dict) -> Layer:
        """Load the attributes in the dictionary d into self."""

        self.size = d['size']
        self.weights = d['weights']
        self.bias = d['bias']
        self.activation = activation_by_name(d['activation'])
        self.neurons = d['neurons']