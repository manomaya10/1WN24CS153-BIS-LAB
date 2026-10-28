import random

directions = [
    "blr - mys",
    "mys - blr",
    "tum - kol",
    "kol - tum"
]

traffic = [35, 30, 50, 45]

cycle_time = 120
min_green = 15
max_green = 50

num_particles = 5
iterations = 50

w = 0.7
c1 = 1.5
c2 = 1.5


def calculate_waiting_time(green_times):

    total_waiting = 0

    for i in range(4):
        red_time = cycle_time - green_times[i]
        average_wait = red_time / 2
        waiting = traffic[i] * average_wait
        total_waiting += waiting

    excess = sum(green_times) - cycle_time

    if excess > 0:
        total_waiting += excess * 100

    return total_waiting


particles = []

for i in range(num_particles):

    position = [
        random.uniform(min_green, max_green)
        for _ in range(4)
    ]

    velocity = [
        random.uniform(-5, 5)
        for _ in range(4)
    ]

    particles.append({
        "position": position,
        "velocity": velocity,
        "pbest": position.copy(),
        "pbest_fitness": calculate_waiting_time(position)
    })


gbest = min(
    particles,
    key=lambda particle: particle["pbest_fitness"]
)

gbest_position = gbest["pbest"].copy()
gbest_fitness = gbest["pbest_fitness"]


for iteration in range(iterations):

    for particle in particles:

        position = particle["position"]
        velocity = particle["velocity"]

        for i in range(4):

            r1 = random.random()
            r2 = random.random()

            velocity[i] = (
                w * velocity[i]
                + c1 * r1 * (particle["pbest"][i] - position[i])
                + c2 * r2 * (gbest_position[i] - position[i])
            )

        for i in range(4):

            position[i] += velocity[i]

            position[i] = max(
                min_green,
                min(max_green, position[i])
            )

        current_fitness = calculate_waiting_time(position)

        if current_fitness < particle["pbest_fitness"]:

            particle["pbest"] = position.copy()
            particle["pbest_fitness"] = current_fitness

        if current_fitness < gbest_fitness:

            gbest_position = position.copy()
            gbest_fitness = current_fitness

print("---TRAFFIC SIGNAL OPTIMIZATION USING PSO---")
print(" FINAL Pbest OF EACH PARTICLE")

for i, particle in enumerate(particles):

    print(
        "Particle", i + 1,
        "PBest:",
        [round(x, 2) for x in particle["pbest"]],
        "Fitness:",
        round(particle["pbest_fitness"], 2)
    )


print("\n FINAL Gbest")

for i in range(4):
    print(
        directions[i],
        ":",
        round(gbest_position[i], 2),
        "seconds"
    )

print("\nGBest Fitness:",
      round(gbest_fitness, 2))

print("Total Green Time:",
      round(sum(gbest_position), 2),
      "seconds")
print("\noptimisation done using pso")