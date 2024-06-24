# Genetic Algorithm Template

Template of implementation of the genetic algorithm on neural networks (NNs), written in python.

## Basic Requirements
1. [Python](https://www.python.org/downloads/).
2. Souce code of a game (or problem) that you wish to generate a NN for, which satisfies the following requirements:
   - The player has finite options (output layer in NN must be finite and realistically fairly small due to computational limitations).
   - The player can be easily simulated in it's environment (see [Simulator](#Simulator)).
   - It is possible to define when the player is doing well (see [Fitness](#Fitness)).

## Getting Started
- If using [Poetry](https://python-poetry.org/docs/) simply use the command `poetry add git+https://github.com/RJW20/genetic-algorithm-template.git`.
- If not using Poetry download just the `genetic_algorithm` folder and place it in the root of your current project directory, and ensure you have the latest version of [NumPy](https://numpy.org/) installed.

In both cases, also download/copy all contents of `example_template` and place them in a `src/` folder or whatever directory it is you're going to be working in.

## Using the Template

### Player Class
Either fill out all methods described or let the player class also extend the class for whatever player exists in the game and ensure it has some of the methods there. You will need to fill out the look and think methods to set the player's genome inputs and feed them in to the NN.

### Simulator
This is where the player will be simulated in its environment. All rules of the game the player is a part of must be present and you should collect stats on how the player performs to feed into the `calculate_fitness` function.

### Fitness
This is a value determining how good a player is. In the simplest case this can just be a player's score.

### Configuring the Settings

#### `player_args`
A dictionary of the arguments you need to start a new instance of your player class.

#### `genetic_algorithm_settings`
The settings dictating how the genetic algorithm creates and evolves the population of players.
1. Population Properties:
  - `population_size`: How many players to simulate in every generation.
  - `creation_type`: `new` to create a newly randomized population or `load` to load a previous save of parents and repopulate from there.
  - `load_folder`: Folder where the parents to load from are saved (if applicable).
  - `parents_folder`: Folder to save parents of each generation to (will be overwritten each time).
  - `total_generations`: Number of iterations of the algorithm.
2. History Properties:
  - `history_folder`: Folder to save the best performing NN's of each generation.
  - `history_type`: Describes what will be saved each generation.
  - `history_value`: Works with `history_type`.
3. Genome Properties:
  - `structure`: The structure of the genome's NN. This must be of type tuple[tuple[int, str], ...] where the int value is how many nodes to have in the layer and string value is the activation function for that layer (options are 'sigmoid', 'relu', 'softmax', 'linear'). Note the node count for the first layer must be the same as the number of inputs that are being fed into the genome and for the last layer must be the same as the number of possible moves a player has.
4. Evolution Properties:
  - `parent_percentage`: (Decimal) percentage of parents to create the next generation from.
  - `crossover_type`: Describes how offspring will be generated from parents.
  - `mutation_type`: Desribes how offspring will mutate.
  - `mutation_rate`: (Decimal) percentage of how many genes to mutate in a genome.

#### `simulation_settings`
Any constants or values that every simulation of the game needs to set up the environment for the player in the `simulate` function.

## Running the Algorithm
Run the function `main` in `main.py` from the template.

## Examples
- [Snake](https://github.com/RJW20/snake_ai_genetic_algorithm_v2)
- [Flappy Bird](https://github.com/RJW20/flappy_bird_ai_genetic_algorithm)
