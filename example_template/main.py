from multiprocessing import Pool

from genetic_algorithm import Population
from .player import Player
from .simulator import simulate
from settings import player_args


#bind settings to variables
from settings import genetic_algorithm_settings
population_size = genetic_algorithm_settings['population_size']
creation_type = genetic_algorithm_settings['creation_type']
load_folder = genetic_algorithm_settings['load_folder']
parents_folder = genetic_algorithm_settings['parents_folder']
total_generations = genetic_algorithm_settings['total_generations']
history_folder = genetic_algorithm_settings['history_folder']
history_type = genetic_algorithm_settings['history_type']
history_value = genetic_algorithm_settings['history_value']
structure = genetic_algorithm_settings['structure']
parent_percentage = genetic_algorithm_settings['parent_percentage']
crossover_type = genetic_algorithm_settings['crossover_type']
mutation_type = genetic_algorithm_settings['mutation_type']
mutation_rate = genetic_algorithm_settings['mutation_rate']


def main() -> None:

    #initialize the population of players    
    players = [Player(**player_args) for _ in range(population_size)]
    population = Population(population_size, players)

    #add their Genomes
    match(creation_type):
        case 'new':
            population.new_genomes(structure)
        case 'load':
            population.load(load_folder)
            population.repopulate(crossover_type, mutation_type, mutation_rate)

    #evolve
    while population.current_generation <= total_generations:

        #run the players with multiprocessing
        with Pool() as pool:
            population.players = pool.map(simulate, population.players, chunksize=1)

        #print some stats
        print(f'\ngeneration: {population.current_generation}, champ\'s best score: {population.champ.best_score}, ' + 
              f'best fitness: {round(population.champ.fitness)}, average fitness: {round(population.average_fitness)}, ', end = '')

        #add to history
        population.save_history(history_folder, history_type, history_value)

        #remove the poorly perfoming players and report the improvements
        population.cull(parent_percentage)
        print(f'average parent fitness: {round(population.average_fitness)}\n')

        #save the parents
        population.save_parents(parents_folder)

        #repopulate in preparation to repeat
        population.repopulate(crossover_type, mutation_type, mutation_rate)