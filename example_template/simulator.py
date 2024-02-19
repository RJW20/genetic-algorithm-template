from .player import Player
from settings import simulation_settings


def calculate_fitness(**stats: dict) -> float:
    """Return a value determining how 'good' a player is.
    
    This will be a function of stats.
    """
    
    return .0


def simulate(player: Player) -> Player:
    """Assign the player its fitness.
    
    Run the player in its environment dependent on simulation_settings.
    Collect stats and then calculate the fitness of the player and assign it.
    """
    stats = dict()
    simulation_settings #to be used here

    while not player.is_dead:
        player.look()
        move = player.think()
        player.move(move)

        #edit stats after each move

    player.fitness = calculate_fitness(**stats)
    return player