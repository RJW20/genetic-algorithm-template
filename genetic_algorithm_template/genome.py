from __future__ import annotations
from copy import deepcopy

import numpy as np


class Genome:
    """Neural network of given structure."""

    def feed_forward(self, input):
        """Return the final layer neurons obtained from feeding forward the given input.
        
        The input must already be in order and normalized.
        """

    def __eq__(self, other):

    def clone(self) -> Genome:
        """Return a deepcopy of self."""

    def save(self, file_name, folder_name):
        """Save neural network parameters to .npz."""

    @classmethod
    def load(cls, file_name, folder_name):
        """Load a neural network from a .npz file.
        
        The file must already exist.
        The structure is gleaned from the file."""