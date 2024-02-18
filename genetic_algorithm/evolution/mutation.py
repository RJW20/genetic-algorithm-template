from typing import Callable

import numpy as np

from ..genome import Genome


def gaussian_mutation(genome: Genome, mutation_rate: float) -> None:
    """Perform a gaussian mutation for each gene in a Genome with probability mutation_rate.
    
    Each gene selected for mutation will have a value ~N(0,0.2) added to it.
    If a genes value becomes out of the range [-1,1] it will be clipped to it.
    """

    for layer in genome.layers:
        for arr in [layer.bias, layer.weights]:
                mutation = np.random.normal(size=arr.shape) * 0.2
                mask = np.random.random(size=arr.shape) < mutation_rate
                arr[mask] += mutation[mask]
                np.clip(arr, -1, 1, out=arr)


def uniform_mutation(genome: Genome, mutation_rate: float) -> None:
    """Randomly mutate each gene in a Genome with probability mutation_rate.
    
    Each gene selected for mutation will be assigned a new value ~U[-1,1].
    """

    for layer in genome.layers:
        for arr in [layer.bias, layer.weights]:
                mutation = np.random.uniform(-1, 1, size=arr.shape)
                mask = np.random.random(size=arr.shape) < mutation_rate
                arr[mask] += mutation[mask]


def mutation_by_name(name: str) -> Callable[[Genome, float], None]:
    """Return mutation function from name."""

    mutations = {
        'gaussian': gaussian_mutation,
        'uniform': uniform_mutation,
    }
    
    try:
        mutation = mutations[name.lower()]
    except KeyError:
         raise Exception(f"Invalid mutation function {name}")

    return mutation