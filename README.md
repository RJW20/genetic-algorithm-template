# Genetic Algorithm Template

Template of implementation of the genetic algorithm on neural networks, written in python.

## Basic Requirements
1. [Python](https://www.python.org/downloads/).
2. Souce code of a game (or problem) that you wish to generate a NN for, which satisfies the following requirements:
   - The player has finite options (output layer in NN must be finite and realistically fairly small due to computational limitations).
   - The player can be easily simulated in it's environment (see [Simulator](#Simulator)).
   - It is possible to define when the player is doing well (see [Fitness](#Fitness)).

## Getting Started
If using [Poetry](https://python-poetry.org/docs/):
- Download the entire repo and place it in folder `libs/`.
- Under `[tool.poetry.dependencies]` in your `pyproject.toml` file add `genetic_algorithm = { path = "libs/genetic_algorithm_template/", develop = false }`.
- Add [Numpy](https://numpy.org/) with `poetry add numpy`.

If not using Poetry:
- Download just the `genetic_algorithm` folder and place it in the root of your current project directory.
- Make sure you have the latest version of [NumPy](https://numpy.org/) installed.

In both cases, also copy all files from the `example_template` and place them in a `src/` folder or whatever folder it is your going to be working in.

## Using the Template

### Player Class
Either fill out all methods described or let the player class also extend the class for whatever player exists in the game and ensure it has some of the methods there. You will need to fill out the look and think methods to set the player's genome inputs and feed them in to the NN.

### Simulator
This is where the player will be simulated in its environment. All rules of the game the player is a part of must be present and you should collect stats on how the player performs to feed into the `calculate_fitness` function.

#### Fitness
This is a value determining how good a player is. In the simplest case this can just be a player's score.

### Configuring the Settings

#### `player_args`
A dictionary of the arguments you need to start a new instance of your player class.

#### `genetic_algorithm_settings`
The settings dictating how the genetic algorithm creates and evolves the population of players:
- 

#### `simulation_settings`

## Running the Algorithm

