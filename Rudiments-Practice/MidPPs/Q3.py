import random

# Optional: Uncomment the line below to get the exact same results every time you run it
# random.seed(42) 

# --- Helper Functions ---
def fitness_function(x):
    return (x**2) - (3*x) + 4

def encode(x):
    """Converts an integer (0-15) to a 4-bit binary string."""
    return format(x, '04b')

def decode(chromosome_str):
    """Converts a 4-bit binary string back to an integer."""
    return int(chromosome_str, 2)

# --- GA Operators ---
def roulette_wheel_selection(population, fitnesses):
    """Selects parents based on their fitness weight."""
    total_fitness = sum(fitnesses)
    # If total fitness is 0 (unlikely here), give equal weights
    if total_fitness == 0:
        probabilities = [1/len(population)] * len(population)
    else:
        probabilities = [f / total_fitness for f in fitnesses]
        
    # random.choices picks elements with specified weights/probabilities
    selected_parents = random.choices(population, weights=probabilities, k=len(population))
    return selected_parents

def single_point_crossover(parent1, parent2):
    """Swaps bits between two parents at a random crossover point."""
    # Choose a point between 1 and 3 (so we don't just swap the whole string or nothing)
    point = random.randint(1, 3)
    offspring1 = parent1[:point] + parent2[point:]
    offspring2 = parent2[:point] + parent1[point:]
    return offspring1, offspring2, point

def mutate(chromosome, mutation_rate=0.1):
    """Flips bits in the chromosome based on the mutation probability."""
    mutated_chromosome = ""
    mutations_occurred = False
    for bit in chromosome:
        if random.random() < mutation_rate:
            # Flip the bit
            mutated_chromosome += "0" if bit == "1" else "1"
            mutations_occurred = True
        else:
            mutated_chromosome += bit
    return mutated_chromosome, mutations_occurred

# --- Main Simulation ---
def simulate_genetic_algorithm():
    print("=== GENETIC ALGORITHM SIMULATION (1 GENERATION) ===\n")

    # a. Encode a random initial population of 4 chromosomes
    initial_decimals = [random.randint(0, 15) for _ in range(4)]
    population = [encode(x) for x in initial_decimals]
    
    print("a. Initial Population:")
    for i, chrom in enumerate(population):
        print(f"   C{i+1}: {chrom} (Decimal: {decode(chrom)})")

    # b. Decode and compute fitness
    fitnesses = [fitness_function(decode(chrom)) for chrom in population]
    
    print("\nb. Fitness Evaluation:")
    for i, chrom in enumerate(population):
        print(f"   C{i+1} ({chrom}) -> x={decode(chrom)}, f(x) = {fitnesses[i]}")

    # c. Perform one round of selection, crossover, and mutation
    print("\nc. Evolution Process:")
    
    # 1. Selection
    parents = roulette_wheel_selection(population, fitnesses)
    print(f"   Selected Parents (via Roulette Wheel): {parents}")
    
    # 2. Crossover
    next_generation = []
    # Pair them up: (0 with 1) and (2 with 3)
    for i in range(0, 4, 2):
        p1, p2 = parents[i], parents[i+1]
        o1, o2, cross_point = single_point_crossover(p1, p2)
        print(f"   Crossover between {p1} and {p2} at index {cross_point}:")
        print(f"      -> Offspring: {o1}, {o2}")
        next_generation.extend([o1, o2])
        
    # 3. Mutation
    final_generation = []
    print("   Applying Mutation (Probability = 0.1 per bit):")
    for i, chrom in enumerate(next_generation):
        mutated_chrom, did_mutate = mutate(chrom, 0.1)
        if did_mutate:
            print(f"      Mutated {chrom} -> {mutated_chrom}")
        final_generation.append(mutated_chrom)

    # d. Identify the best chromosome
    print("\nd. Next Generation Results:")
    new_fitnesses = [fitness_function(decode(chrom)) for chrom in final_generation]
    
    best_fitness = -float('inf')
    best_chromosome = ""
    
    for i, chrom in enumerate(final_generation):
        dec = decode(chrom)
        fit = new_fitnesses[i]
        print(f"   O{i+1}: {chrom} (x={dec}) -> Fitness: {fit}")
        
        if fit > best_fitness:
            best_fitness = fit
            best_chromosome = chrom
            
    print(f"\n🏆 BEST CHROMOSOME THIS GENERATION:")
    print(f"   Binary: {best_chromosome}")
    print(f"   Decimal: {decode(best_chromosome)}")
    print(f"   Fitness: {best_fitness}")

# Run the program
simulate_genetic_algorithm()