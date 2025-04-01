import random
import math
import json
import os
import matplotlib.pyplot as plt

# Configurações
NUM_CITIES = 20
POPULATION_SIZE = 200
GENERATIONS = 500
BASE_MUTATION_RATE = 0.1
OPTIMAL_DISTANCE = 300  # Alvo desejado
OPTIMAL_FITNESS = 1 / OPTIMAL_DISTANCE

# Arquivo onde as cidades serão salvas
CITY_FILE = "cities.json"

# Gerar ou carregar cidades
def load_or_generate_cities():
    if os.path.exists(CITY_FILE):
        with open(CITY_FILE, "r") as f:
            return json.load(f)
    else:
        cities = [(random.uniform(0, 100), random.uniform(0, 100)) for _ in range(NUM_CITIES)]
        with open(CITY_FILE, "w") as f:
            json.dump(cities, f)
        return cities

cities = load_or_generate_cities()

# Converter para tupla (json salva como lista)
cities = [tuple(city) for city in cities]

# Distância Euclidiana
def euclidean_distance(a, b):
    return math.hypot(a[0] - b[0], a[1] - b[1])

# Matriz de distâncias
distances = [[euclidean_distance(c1, c2) for c2 in cities] for c1 in cities]

class Individual:
    def __init__(self, genes=None):
        if genes:
            self.genes = genes
        else:
            self.genes = list(range(NUM_CITIES))
            random.shuffle(self.genes)
        self.fitness = self.evaluate_fitness()

    def evaluate_fitness(self):
        total_distance = 0
        for i in range(NUM_CITIES):
            from_city = self.genes[i]
            to_city = self.genes[(i + 1) % NUM_CITIES]
            total_distance += distances[from_city][to_city]
        return 1 / total_distance

def crossover(parent1, parent2):
    start, end = sorted(random.sample(range(NUM_CITIES), 2))
    child_genes = [None] * NUM_CITIES
    child_genes[start:end] = parent1.genes[start:end]

    pointer = 0
    for gene in parent2.genes:
        if gene not in child_genes:
            while child_genes[pointer] is not None:
                pointer += 1
            child_genes[pointer] = gene

    return Individual(child_genes)

def mutate(individual, mutation_rate):
    if random.random() < mutation_rate:
        i, j = random.sample(range(NUM_CITIES), 2)
        individual.genes[i], individual.genes[j] = individual.genes[j], individual.genes[i]
        individual.fitness = individual.evaluate_fitness()

def tournament_selection(population):
    return max(random.sample(population, 2), key=lambda ind: ind.fitness)

# Inicialização
distance_progress = []
population = [Individual() for _ in range(POPULATION_SIZE)]
best_individual = max(population, key=lambda ind: ind.fitness)
best_distance = 1 / best_individual.fitness
stagnant_generations = 0

for generation in range(GENERATIONS):
    new_population = []

    if stagnant_generations >= 20:
        mutation_rate = min(0.9, BASE_MUTATION_RATE * 2)
    else:
        mutation_rate = BASE_MUTATION_RATE

    # Elitismo
    new_population.append(best_individual)

    while len(new_population) < POPULATION_SIZE - 2:
        parent1 = tournament_selection(population)
        parent2 = tournament_selection(population)
        child = crossover(parent1, parent2)
        mutate(child, mutation_rate)
        new_population.append(child)

    new_population.append(Individual())
    new_population.append(Individual())

    population = new_population
    current_best = max(population, key=lambda ind: ind.fitness)
    current_distance = 1 / current_best.fitness

    if current_distance < best_distance:
        best_individual = current_best
        best_distance = current_distance
        stagnant_generations = 0
    else:
        stagnant_generations += 1

    distance_progress.append(best_distance)
    print(f"Geração {generation}: Melhor distância = {best_distance:.2f}")

    if current_best.fitness >= OPTIMAL_FITNESS:
        print(f"\nSolução satisfatória atingida na geração {generation} com distância {current_distance:.2f}")
        break

print("\nMelhor rota encontrada:")
print(best_individual.genes)
print(f"Distância total: {best_distance:.2f}")

x = [cities[i][0] for i in best_individual.genes] + [cities[best_individual.genes[0]][0]]
y = [cities[i][1] for i in best_individual.genes] + [cities[best_individual.genes[0]][1]]

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.plot(distance_progress)
plt.title("Evolução da Distância (TSP)")
plt.xlabel("Geração")
plt.ylabel("Distância da Melhor Rota")
plt.grid(True)

plt.subplot(1, 2, 2)
plt.plot(x, y, marker='o')
plt.title("Melhor Rota Encontrada")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)

plt.tight_layout()
plt.show()
