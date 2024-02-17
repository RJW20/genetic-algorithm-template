from __future__ import annotations
from copy import deepcopy
import os

import numpy as np

from .evolution.layer import Layer
from .activation_functions import sigmoid, relu, softmax, linear, activation_by_name

class Genome:
    """Neural network of given structure."""

    __slots__ = (
        "birth_gen",
        "layers",
    )

    def __init__(self, birth_gen: int = 1) -> None:
        self.birth_gen = birth_gen
        self.layers = tuple()

    @classmethod
    def new(cls, birth_gen: int, structure: tuple[tuple[int,str]]) -> Genome:
        """Return a newly randomized Genome with given structure.
        
        Structure must be a tuple of tuples (size, activation).
        """

        genome = cls(birth_gen)
        for _, layer_properties in enumerate(structure):
            size = layer_properties[0]
            activation = activation_by_name(layer_properties[1])
            genome.layers.append(Layer.new(size, activation))

        return genome

    def propagate(self, input: np.array) -> np.array:
        """Return the final layer neurons obtained from feeding forward the given input.
        
        The input must already be in order and normalized.
        """

        self.layers[0].propagate(input)
        for layer_no, layer in enumerate(self.layers[1:]):
            layer.propagate(self.layers[layer_no-1].neurons)

        return self.layers[-1].neurons

    def __eq__(self, other):
        """Return True if both Genomes have the same structure and parameters."""

        if (depth := len(self.layers)) != len(other.layers): return False
        for i in range(depth):
            if self.layers[i] != other.layers[i]: return False
        return True

    def clone(self) -> Genome:
        """Return a deepcopy of self."""

        return deepcopy(self)

    def save(self, file_name: str, folder_name: str) -> None:
        """Save neural network parameters to .npz."""

        #check folder exists, create if it doesn't
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

        #create a dictionary of the genome and its layers
        savez_dict = dict()
        savez_dict['birth_gen'] - self.birth_gen
        savez_dict['structure'] = np.array([(24, b'none')] + [(layer.size, str(layer.activation)) for layer in self.layers], dtype='int,S8')
        for i, layer in enumerate(self.layers):
            savez_dict[f'{i}_weights'] = layer.weights
            savez_dict[f'{i}_bias'] = layer.bias

        #save the file
        np.savez(f'{folder_name}/{file_name}', **savez_dict)

    @classmethod
    def load(cls, file_name: str, folder_name: str) -> Genome:
        """Load a neural network from a .npz file.
        
        The file must already exist.
        The structure is gleaned from the file.
        """

        genome = cls()
        
        #load the dictionary of files and the structure
        genome_dict = np.load(f'{folder_name}/{file_name}')
        genome.birth_gen = genome_dict['birth_gen']
        structure = genome_dict['structure']

        #add the layers into the genome
        for coord, layer_properties in np.ndenumerate(structure[1:]):
            layer = Layer(layer_properties[0], activation_by_name(layer_properties[1].decode('utf-8')))
            layer.weights = genome_dict[f'{coord[0]}_weights']
            layer.bias = genome_dict[f'{coord[0]}_bias']
            genome.layers.append(layer)

        return genome