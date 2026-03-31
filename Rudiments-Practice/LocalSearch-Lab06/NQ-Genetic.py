import random

# 1. Define the size of the board (N-Queens)
n = 8  
population_size = 10
mutation_rate = 0.1

# Fitness function: counts non-attacking pairs of queens
def calculate_fitness(individual):
    non_attacking_pairs = 0
    total_pairs = n * (n - 1) // 2 # Maximum possible non-attacking pairs
    
    # Check for conflicts
    for i in range(n):
        for j in range(i + 1, n):
            # No same column or diagonal conflict
            if individual[i] != individual[j] and abs(individual[i] - individual[j]) != abs(i - j):
                non_attacking_pairs += 1
                
    # FIX: Added missing return statement, normalized to a float (0.0 to 1.0)
    return non_attacking_pairs / total_pairs

# Generate a random individual (chromosome) based on column positions
def create_random_individual():
    return random.sample(range(n), n) # Ensure unique column positions

# Select the best routes (parents) based on fitness
def select_parents(population, fitness_scores):
    # Select top 50% of the population
    sorted_population = [board for _, board in sorted(zip(fitness_scores, population), reverse=True)]
    return sorted_population[:len(population) // 2]

# Crossover function: single-point crossover with unique column
def crossover(parent1, parent2):
    point = random.randint(1, n - 2) # Choose a crossover point
    child = parent1[:point] + parent2[point:]
    
    # Ensure unique column positions
    missing = set(range(n)) - set(child)
    for i in range(len(child)):
        if child.count(child[i]) > 1:
            child[i] = missing.pop()
    return child

# Randomly swap two locations in a route
def mutate(route):
    # FIX: Changed 'individual' to 'route' to match function parameter
    idx1, idx2 = random.sample(range(n), 2)
    route[idx1], route[idx2] = route[idx2], route[idx1]
    return route

# Genetic Algorithm main function
def genetic_algorithm():
    population = [create_random_individual() for _ in range(population_size)]
    generation = 0
    best_fitness = 0
    best_individual = []
    
    # Increased generation limit to 1000 to give it time to find a solution
    while best_fitness < 1.0 and generation < 1000:
        fitness_scores = [calculate_fitness(ind) for ind in population]
        best_fitness = max(fitness_scores)
        best_individual = population[fitness_scores.index(best_fitness)]
        
        print(f"Generation {generation} Best Fitness: {best_fitness:.4f}")
        
        # Check for optimal solution
        if best_fitness == 1.0:
            break
            
        # Selection
        parents = select_parents(population, fitness_scores)
        
        # Crossover
        new_population = []
        for _ in range(population_size):
            parent1, parent2 = random.sample(parents, 2)
            child = crossover(parent1, parent2)
            new_population.append(child)
            
        # Mutation
        for i in range(len(new_population)):
            if random.random() < mutation_rate:
                new_population[i] = mutate(new_population[i])
                
        population = new_population
        generation += 1
        
    return best_individual, best_fitness

# Run the Genetic Algorithm cleanly
if __name__ == "__main__":
    print(f"--- Starting GA for {n}-Queens ---")
    solution, fitness = genetic_algorithm()
    print("\n--- Final Results ---")
    print("Best Solution (Column indices per row):", solution)
    print(f"Best Fitness: {fitness:.4f}")
    if fitness == 1.0:
        print("Status: Optimal Solution Found!")
    else:
        print("Status: Stuck in local optima. Try increasing population size or generation limit.")