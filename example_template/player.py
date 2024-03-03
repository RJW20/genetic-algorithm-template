from typing import Any
from copy import deepcopy

import numpy as np

from genetic_algorithm import BasePlayer


class Player(BasePlayer):
    """Example of a Player class.
    
    All these methods must be present.
    """

    def __init__(self, **kwargs) -> None:
        self.score: int = 0
        self.fitness: int = 0
        self.best_score: int = 0

    def look(self) -> None:
        """Update the attributes used as input to the Genome."""
        pass

    def think(self) -> Any:
        """Feed the input into the Genome and turn the output into a valid move."""

        genome_input = np.array([])     #some function of the vision found in self.look()
        self.genome.propagate(genome_input)

    def move(self, move: Any) -> None:
        """Advance to the state achieved by carrying out move."""
        pass

    @property
    def is_dead(self) -> bool:
        """Return True if the player has reached a state where the game is over."""
        pass

    def start_state(self) -> None:
        """Put player in a state to begin simulation in its environment."""
        self.score = 0