import numpy as np

from genetic_algorithm.base_player import BasePlayer


def fitness_weighted_selection(parents: list[BasePlayer]) -> tuple[BasePlayer, BasePlayer]:
    """Picks 2 parents at rate proportional to their fitness."""

    wheel = sum(parent.fitness for parent in parents)
    probabilities = [parent.fitness/wheel for parent in parents]
    selection = np.random.choice(parents, 2, replace=False, p=probabilities)

    return selection[0], selection[1]