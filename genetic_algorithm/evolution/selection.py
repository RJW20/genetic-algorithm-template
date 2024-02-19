import numpy as np

from genetic_algorithm.base_player import BasePlayer


def fitness_weighted_selection(parents: list[BasePlayer]) -> tuple[BasePlayer, BasePlayer]:
    """Picks 2 parents at rate proportional to their fitness.
    
    Requires all parents have fitness >= 0.
    Requires at least 2 parents have fitness > 0.
    """

    fitness_table = [parent.fitness for parent in parents]
    min_fitness = min(fitness_table)
    max_fitness = max(fitness_table)
    sum_fitness = sum(fitness_table)

    if min_fitness < 0:
        raise Exception("To use fitness_weighted_selection all parents must have a fitness " +
                        "greater than or equal to zero. Please edit the calculate_fitness function.")

    if max_fitness == sum_fitness:
        raise Exception("To use fitness_weighted_selection at least two parents must have a " + 
                        "strictly positive fitness. Please edit the calculate_fitness function.")

    wheel = sum(parent.fitness for parent in parents)
    probabilities = [parent.fitness/wheel for parent in parents]
    selection = np.random.Generator.choice(parents, 2, replace=False, p=probabilities, axis=0, shuffle=False)

    return selection[0], selection[1]