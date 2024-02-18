from typing import Callable, Literal

import numpy as np

from ..genome import Genome


def one_point_crossover(parent1: Genome, parent2: Genome, gen: int) -> tuple[Genome, Genome]:
    """Return a crossover of two Genomes with randomly chosen proportion from each.
    
    The genomes must always have the same structure.
    """

    offspring1 = parent1.clone()
    offspring2 = parent2.clone()
    offspring1.birth_gen = offspring2.birth_gen = gen

    crossover_rate = np.random.uniform(0,1)
    for i, (l1, l2) in enumerate(zip(parent1.layers, parent2.layers)):

        weights_mask = np.random.uniform(0, 1, size=l1.weights.shape)
        offspring1.layers[i].weights[weights_mask > crossover_rate] = l2.weights[weights_mask > crossover_rate]
        offspring2.layers[i].weights[weights_mask > crossover_rate] = l1.weigths[weights_mask > crossover_rate]

        bias_mask = np.random.uniform(0, 1, size=l1.bias.shape)
        offspring1.layers[i].bias[bias_mask > crossover_rate] = l2.bias[bias_mask > crossover_rate]
        offspring2.layers[i].bias[bias_mask > crossover_rate] = l1.bias[bias_mask > crossover_rate]

    return offspring1, offspring2


def uniform_crossover(parent1: Genome, parent2: Genome, gen: int) -> tuple[Genome, Genome]:
    """Return a crossover of two Genomes with 50:50 proportion from each.
    
    The genomes must always have the same structure.
    """

    offspring1 = parent1.clone()
    offspring2 = parent2.clone()
    offspring1.birth_gen = offspring2.birth_gen = gen

    for i, (l1, l2) in enumerate(zip(parent1.layers, parent2.layers)):

        weights_mask = np.random.uniform(0, 1, size=l1.weights.shape)
        offspring1.layers[i].weights[weights_mask > 0.5] = l2.weights[weights_mask > 0.5]
        offspring2.layers[i].weights[weights_mask > 0.5] = l1.weigths[weights_mask > 0.5]

        bias_mask = np.random.uniform(0, 1, size=l1.bias.shape)
        offspring1.layers[i].bias[bias_mask > 0.5] = l2.bias[bias_mask > 0.5]
        offspring2.layers[i].bias[bias_mask > 0.5] = l1.bias[bias_mask > 0.5]

    return offspring1, offspring2
    

def crossover_by_name(name: Literal['one-point', 'uniform']) -> Callable[[Genome, Genome, int], tuple[Genome, Genome]]:
    """Return crossover function from name."""

    crossovers = {
        'one-point': one_point_crossover,
        'uniform': uniform_crossover,
    }

    try:
        crossover = crossovers[name]
    except KeyError:
        raise TypeError(f"Invalid crossover function{name}")

    return crossover