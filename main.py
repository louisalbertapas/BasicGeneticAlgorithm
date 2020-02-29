import utils


def main():
    population_size = 0
    user_input_number = input("Enter number of population[2 or more]: ")
    try:
        population_size = int(user_input_number)
        if population_size < 2:
            print("Incorrect population type. Defaulting to 10")
            population_size = 10
            input("Press enter to continue...")
    except ValueError:
        print("Please enter integer type.")
        exit(0)

    generation = 1
    population = utils.populate_initial_genes(population_size)

    print(utils.Constants.LABEL_GENERATION_START)
    for obj in population[0:10]:
        print(obj.name, obj.fitness)
    print(utils.Constants.LABEL_GENERATION_DONE)

    while population[0].name != utils.Constants.STRING_TO_MUTATE:
        print(utils.Constants.LABEL_GENERATION_START)
        population = utils.mutate_genes(population, population_size)

        for obj in population[0:10]:
            print(obj.name, obj.fitness)

        generation += 1
        print(utils.Constants.LABEL_GENERATION_DONE)

    print(utils.Constants.LABEL_GENERATION, generation)


if __name__ == '__main__':
    main()
