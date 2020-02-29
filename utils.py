import random
import string


class Constants:
    STRING_TO_MUTATE = "HelloWorld"
    LENGTH_OF_STRING_TO_MUTATE = len(STRING_TO_MUTATE)
    LABEL_GENERATION_START = "========START OF GENERATION========="
    LABEL_GENERATION_DONE = "=========END OF GENERATION=========="
    LABEL_GENERATION = "Number of generations: "


class Gene:
    def __init__(self, name, fitness):
        self.name = name
        self.fitness = fitness


def generate_random_character():
    character = random.choice(string.ascii_letters)
    return character


def generate_random_string():
    i = 0
    name = ""
    while i < Constants.LENGTH_OF_STRING_TO_MUTATE:
        name += generate_random_character()
        i += 1
    return name


def calculate_fitness(name):
    i = 0
    fitness = 0
    while i < Constants.LENGTH_OF_STRING_TO_MUTATE:
        if name[i] == Constants.STRING_TO_MUTATE[i]:
            fitness += 1
        i += 1

    return fitness


def sort_population(population):
    new_list = sorted(population, key=lambda gene: gene.fitness, reverse=True)
    return new_list


def populate_initial_genes(population_size):
    unsorted_population = []

    while population_size > 0:
        name = generate_random_string()
        fitness = calculate_fitness(name)
        unsorted_population.append(Gene(name, fitness))
        population_size -= 1

    return sort_population(unsorted_population)


def generate_new_name(parent_x, parent_y):
    i = 0
    child_string = ""
    while i < Constants.LENGTH_OF_STRING_TO_MUTATE:
        if random.randint(0, 1) == 1:
            child_string += parent_x[i]
        else:
            child_string += parent_y[i]
        i += 1

    if random.randint(0, 100) <= 5:
        index_to_mutate = random.randint(0, Constants.LENGTH_OF_STRING_TO_MUTATE - 1)
        child_string = child_string[:index_to_mutate] + generate_random_character() + child_string[index_to_mutate + 1:]

    return child_string


def mutate_genes(population, population_size):
    old_population = population.copy()
    i = 0

    while i < 2:
        population[i] = old_population[i]
        i += 1

    while i < population_size:
        parent_x_index = random.randint(0, int(population_size / 10))
        parent_y_index = random.randint(0, population_size - 1)

        population[i].name = generate_new_name(old_population[parent_x_index].name, old_population[parent_y_index].name)
        population[i].fitness = calculate_fitness(population[i].name)

        i += 1

    return sort_population(population)
