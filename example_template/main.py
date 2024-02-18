from multiprocessing import Pool

from genetic_algorithm import Population
from player import Player
from settings import player_args
from settings import genetic_algorithm_settings
from simulator import simulate


def main() -> None:

    #initialize the population of players
    creation_type = genetic_algorithm_settings['creation_type']
    population_size = genetic_algorithm_settings['population_size']
    players = [Player(**player_args) for _ in range(population_size)]
    population = Population(population_size, players, 1)

    #add their Genomes
    match(creation_type):
        case 'new':
            structure = genetic_algorithm_settings['structure']
            population.new_genomes(structure)
        case 'load':
            load_folder = genetic_algorithm_settings['load_folder']
            population.load(load_folder)

    #pull out some settings
    parent_percentage = genetic_algorithm_settings['parent_percentage']
    crossover_type = genetic_algorithm_settings['crossover_type']
    mutation_type = genetic_algorithm_settings['mutation_type']
    mutation_rate = genetic_algorithm_settings['mutation_rate']

    #evolve
    total_generations = genetic_algorithm_settings['total_generations']
    while population.current_generation < total_generations:

        #run the players with multiprocessing
        with Pool() as pool:
            population.players = pool.imap_unordered(simulate, population.players, chunksize=1)

        #print some stats
        print(f'\ngeneration: {population.current_generation}, best fitness: {round(population.champ.fitness)}, average fitness: {round(population.average_fitness)}, ', end = '')

        #remove the poorly perfoming players and report the improvements
        population.cull(parent_percentage)
        print(f'average parent fitness: {round(population.average_fitness)}\n')

        #save the progress
        population.champ.genome.save(file_name=population.current_generation, folder_name='champs')
        population.save('latest population')

        #repopulate in preparation to repeat
        population.repopulate(crossover_type, mutation_type, mutation_rate)


