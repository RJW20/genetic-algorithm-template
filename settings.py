

settings = {

    #population properties
    'population_size': 1000,        #number of players in the population
    'creation_type': 'new',         #options are ['new', 'load']
    'parents_folder': '',           #folder to load from if applicable
    'save_folder': '',              #folder to save to
    'total_generations': 500,       #number of generations to run to

    #genome properties
    'structure': ((24, 'none'), (16, 'sgd'), (3, 'softmax')),

    #evolution properties
    'parent_percentage': 0.2,       #percentage of parents to repopulate the next generation from
    'crossover_type': 'one-point',  #options are ['one-point', 'uniform']
    'mutation_type': 'gaussian',    #options are ['gaussian', 'uniform']
    'mutation_rate': 0.05,          #probability a gene will mutate

}