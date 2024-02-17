from abc import ABC, abstractmethod
from __future__ import annotations
from typing import Any

from .genome import Genome

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
        pass

    @abstractmethod
    def think(self) -> None:
        pass

    @abstractmethod
    def move(self, move: Any) -> None:
        pass

    @abstractmethod
    def is_dead(self) -> bool:
        pass

    def __eq__(self, other: BasePlayer) -> bool:
        return self.genome == other.genome
    
    @abstractmethod
    def __pickle__(self):
        pass





