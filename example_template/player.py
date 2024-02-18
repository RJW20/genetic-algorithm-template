from typing import Any

from genetic_algorithm import BasePlayer


class Player(BasePlayer):
    """Example of a Player class.
    
    All these methods must be present.
    """

    def __init__(self, **kwargs) -> None:
        pass

    def look(self) -> None:
        """Update the attributes used as input to the Genome."""
        pass

    def think(self) -> Any:
        """Feed the input into the Genome and turn the output into a valid move."""
        pass

    def move(self, move: Any) -> None:
        """Advance to the state achieved by carrying out move."""
        pass

    @property
    def is_dead(self) -> bool:
        """Return True if the player has reached a state where the game is over."""
        pass

    def __getstate__(self) -> dict:
        """Return a dictionary containing attribute names and their values as (key, value) pairs.
        
        All values must also be pickleable i.e. not use __slots__ or have __getstate__ and __setstate__ methods like this.
        If this class uses __slots__ or extends one that does this must be changed.
        """

        return self.__dict__

    def __setstate__(self, d: dict) -> BasePlayer:
        """Load the attributes in the dictionary d into self.
        
        If this class uses __slots__ or extends one that does this must be changed.
        """

        self.__dict__ = d

    def empty_clone(self) -> BasePlayer:
        """Return a new instance of self's class without a genome."""
        pass