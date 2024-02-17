from functools import cached_property
import numpy as np

from ..base_player import BasePlayer


class FitnessWeightedSelector:
    """Iterator that picks parents at rate proportional to their fitness."""
    
    def __init__(self, players: list[BasePlayer]) -> None:
        self.players = players
        self.last = None

    @cached_property
    def wheel(self) -> float:
        return sum(player.fitness for player in self.players)

    def __iter__(self):
        return self
    
    def __next__(self):
        
        #add something that stops the choice being the same as self.last, but only bothers to do the check if self.last is not none

        pick = np.random.uniform(0, self.wheel)
        running_sum = 0
        for player in self.players:
            running_sum += player.fitness
            if running_sum > pick:
                return player