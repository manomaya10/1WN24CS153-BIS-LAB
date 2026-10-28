import random

employees = [
    "Employee 1",
    "Employee 2",
    "Employee 3",
    "Employee 4",
    "Employee 5"
]

shifts = ["Morning", "Afternoon", "Night"]

availability = [
    ["Morning", "Afternoon"],
    ["Afternoon", "Night"],
    ["Morning", "Night"],
    ["Morning", "Afternoon"],
    ["Afternoon", "Night"]
]

population_size = 6
generations = 50
mutation_rate = 0.1

def fitness(schedule):

    conflicts = 0

    for i in range(len(schedule)):
        if schedule[i] not in availability[i]:
            conflicts += 10

    if schedule.count("Night") > 2:
        conflicts += 5

    if schedule.count("Morning") > 3:
        conflicts += 5

    return conflicts

population = []

for _ in range(population_size):

    chromosome = []

    for i in range(len(employees)):
        chromosome.append(random.choice(shifts))

    population.append(chromosome)

for generation in range(generations):

    population.sort(key=fitness)

    parents = population[:2]

    new_population = []

    while len(new_population) < population_size:

        parent1 = random.choice(parents)
        parent2 = random.choice(parents)

        point = random.randint(1, len(employees) - 1)

        child = parent1[:point] + parent2[point:]

        for i in range(len(child)):

            if random.random() < mutation_rate:
                child[i] = random.choice(shifts)

        new_population.append(child)

    population = new_population

population.sort(key=fitness)

best = population[0]

print("==============================================")
print("    EMPLOYEE SHIFT SCHEDULING USING GA")
print("==============================================")

print("\nFINAL BEST SCHEDULE")
print("----------------------------------------------")

for i in range(len(employees)):
    print(employees[i], ":", best[i])

print("----------------------------------------------")

print("Fitness  :", fitness(best))
print("Conflicts:", fitness(best))

print("\nOptimization completed using Genetic Algorithm.")
