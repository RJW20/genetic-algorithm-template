from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any

from genetic_algorithm.genome import Genome

class BasePlayer(ABC):
    """Abstract base class for a Player in a population."""

    def __init__(self) -> None:
        pass

    @property
    def fitness(self) -> float:
        return self._fitness

    @fitness.setter
    def fitness(self, value: float) -> None:
        self._fitness = value

    @property
    def genome(self) -> Genome:
        return self._genome

    @genome.setter
    def genome(self, value: Genome) -> None:
        self._genome = value

    @abstractmethod
    def look(self) -> None:
        """Update the attributes used as input to the Genome."""
        pass

    @abstractmethod
    def think(self) -> Any:
        """Feed the input into the Genome and turn the output into a valid move."""
        pass

    @abstractmethod
    def move(self, move: Any) -> None:
        """Advance to the state achieved by carrying out move."""
        pass

    @property
    @abstractmethod
    def is_dead(self) -> bool:
        """Return True if the player has reached a state where the game is over."""
        pass

    def __eq__(self, other: BasePlayer) -> bool:
        return self.genome == other.genome
    
    @abstractmethod
    def __getstate__(self) -> dict:
        """Return a dictionary containing attribute names and their values as (key, value) pairs.
        
        All values must also be pickleable i.e. not use __slots__ or have __getstate__ and __setstate__ methods like this.
        """
        pass

    @abstractmethod
    def __setstate__(self, d: dict) -> BasePlayer:
        """Load the attributes in the dictionary d into self."""
        pass

    @abstractmethod
    def empty_clone(self) -> BasePlayer:
        """Return a new instance of self's class without a genome."""
        pass



