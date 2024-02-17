from functools import cached_property

import numpy as np

from ..base_player import BasePlayer


def fitness_weighted_selection(parents: list[BasePlayer]) -> list[BasePlayer, BasePlayer]:
    """Picks 2 parents at rate proportional to their fitness."""

    selection = []
    while len(selection) < 2:
        wheel = sum(parent.fitness for parent in parents)
        pick = np.random.uniform(0, wheel)
        running_sum = 0
        for parent in parents:
            running_sum += parent.fitness
            if running_sum > pick:
                selection.append(parent)
                parents.remove(parent)
                break
    
    return selection