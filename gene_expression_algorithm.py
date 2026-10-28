import random

slots = ["P1", "P2", "P3", "P4", "P5"]

distance = [
    [2, 5, 8, 4, 7],
    [6, 3, 5, 7, 4],
    [7, 6, 2, 5, 4],
    [4, 7, 6, 2, 5],
    [5, 4, 7, 6, 3]
]

population_size = 10
generations = 30
mutation_rate = 0.2

def gene_expression(individual):
    return [slots[gene] for gene in individual]


def fitness(individual):
    total_distance = 0

    for vehicle in range(5):
        total_distance += distance[vehicle][individual[vehicle]]

    return total_distance


population = []

for _ in range(population_size):
    population.append(random.sample(range(5), 5))


best = None
best_fitness = float("inf")


for generation in range(generations):

    for individual in population:

        current_fitness = fitness(individual)

        if current_fitness < best_fitness:
            best = individual.copy()
            best_fitness = current_fitness

    population.sort(key=fitness)

    parent1 = population[0]
    parent2 = population[1]

    point = random.randint(1, 4)

    child = parent1[:point] + parent2[point:]

    used = set()
    missing = [x for x in range(5) if x not in child]

    for i in range(5):
        if child[i] in used:
            child[i] = missing.pop(0)
        else:
            used.add(child[i])

    if random.random() < mutation_rate:
        a, b = random.sample(range(5), 2)
        child[a], child[b] = child[b], child[a]

    population = [parent1, parent2]

    while len(population) < population_size:
        population.append(child.copy())


best_allocation = gene_expression(best)


print("==============================================")
print("     SMART PARKING ALLOCATION USING GEA")
print("==============================================")

print("\nAlgorithm Parameters:")
print("Population Size :", population_size)
print("Generations     :", generations)
print("Mutation Rate   :", mutation_rate)

print("\nFINAL BEST SOLUTION")
print("----------------------------------------------")

for i in range(5):
    print("Vehicle", i + 1, " -> ", best_allocation[i])

print("----------------------------------------------")
print("Best Fitness    :", best_fitness)
print("Total Distance  :", best_fitness)

print("\nGene Expression:")
print("Genes           :", best)
print("Expressed       :", best_allocation)

print("\nOptimization completed using GEA.")
