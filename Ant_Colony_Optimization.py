
import random

distance = [
    [0, 2, 6, 5],
    [2, 0, 4, 2],
    [6, 4, 0, 3],
    [5, 2, 3, 0]
]

N = len(distance)
alpha = 1.0
beta = 2.0
rho = 0.2
Q = 100
number_of_ants = 2
max_iterations = 50

pheromone = [[1.0 for j in range(N)] for i in range(N)]

best_tour = None
best_distance = float('inf')


def calculate_distance(tour):
    total = 0
    for i in range(len(tour) - 1):
        total += distance[tour[i]][tour[i + 1]]
    return total


def construct_tour():
    start = random.randint(0, N - 1)
    tour = [start]
    unvisited = set(range(N))
    unvisited.remove(start)

    while unvisited:
        current = tour[-1]
        cities = list(unvisited)
        weights = []

        for city in cities:
            pheromone_value = pheromone[current][city] ** alpha
            heuristic_value = (1 / distance[current][city]) ** beta
            weights.append(pheromone_value * heuristic_value)

        next_city = random.choices(cities, weights=weights, k=1)[0]
        tour.append(next_city)
        unvisited.remove(next_city)

    tour.append(start)
    return tour


for iteration in range(max_iterations):
    ant_tours = []

    for ant in range(number_of_ants):
        tour = construct_tour()
        tour_distance = calculate_distance(tour)
        ant_tours.append((tour, tour_distance))

        if tour_distance < best_distance:
            best_distance = tour_distance
            best_tour = tour.copy()

    for i in range(N):
        for j in range(N):
            pheromone[i][j] *= (1 - rho)

    for tour, tour_distance in ant_tours:
        deposit = Q / tour_distance

        for i in range(len(tour) - 1):
            city1 = tour[i]
            city2 = tour[i + 1]
            pheromone[city1][city2] += deposit
            pheromone[city2][city1] += deposit

city_names = ['A', 'B', 'C', 'D']

print("ACO FOR TRAVELLING SALESMAN PROBLEM")
print("Best Tour:", " -> ".join(city_names[i] for i in best_tour))
print("Best Distance:", best_distance)