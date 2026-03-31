import random

# Configuration
num_staff = 6 # INCREASED TO 6: 6 staff * 7 shifts = 42 capacity (matches demand)
num_shifts = 21 # 7 days * 3 shifts per day
max_shifts_per_staff = 7
required_staff_per_shift = 2
population_size = 10
mutation_rate = 0.1
max_generations = 1000

# Fitness function (lower is better)
def evaluate_fitness(schedule):
    penalty = 0
    
    # 1. Check shift coverage
    for shift in range(num_shifts):
        assigned_count = sum(schedule[staff][shift] for staff in range(num_staff))
        if assigned_count < required_staff_per_shift:
            penalty += (required_staff_per_shift - assigned_count) * 10
        elif assigned_count > required_staff_per_shift:
            penalty += (assigned_count - required_staff_per_shift) * 5 # Penalize overstaffing too
            
    # 2. Check max shifts per staff (CRITICAL: Crossover can break the initial limit)
    for staff in range(num_staff):
        total_shifts_worked = sum(schedule[staff])
        if total_shifts_worked > max_shifts_per_staff:
            penalty += (total_shifts_worked - max_shifts_per_staff) * 20
            
    return penalty # ADDED MISSING RETURN

# Create a random schedule
def create_random_schedule():
    schedule = [[0] * num_shifts for _ in range(num_staff)]
    for staff in range(num_staff):
        assigned_shifts = random.sample(range(num_shifts), random.randint(3, max_shifts_per_staff))
        for shift in assigned_shifts:
            schedule[staff][shift] = 1
    return schedule

# Selection (Top 50%)
def select_parents(population, fitness_scores):
    sorted_population = [x for _, x in sorted(zip(fitness_scores, population))]
    return sorted_population[:len(population) // 2]

# Crossover (Single point crossover)
def crossover(parent1, parent2):
    point = random.randint(0, num_shifts - 1)
    child = [parent1[i][:point] + parent2[i][point:] for i in range(num_staff)]
    return child

# Mutation (Swap shifts for one staff)
def mutate(schedule):
    staff = random.randint(0, num_staff - 1)
    shift1, shift2 = random.sample(range(num_shifts), 2)
    schedule[staff][shift1], schedule[staff][shift2] = schedule[staff][shift2], schedule[staff][shift1]
    return schedule

# Initial population
population = [create_random_schedule() for _ in range(population_size)]

# Genetic Algorithm loop
for generation in range(max_generations):
    fitness_scores = [evaluate_fitness(schedule) for schedule in population]
    best_fitness = min(fitness_scores)
    
    # Optional: Stop early if a perfect schedule is found
    if best_fitness == 0:
        print(f"Perfect schedule found at Generation {generation + 1}!")
        break
        
    print(f"Generation {generation + 1}, Best Fitness: {best_fitness}")
    
    parents = select_parents(population, fitness_scores)
    new_population = []
    
    # Keep the absolute best parent to prevent regression (Elitism)
    new_population.append(parents[0]) 
    
    while len(new_population) < population_size:
        parent1, parent2 = random.sample(parents, 2)
        child = crossover(parent1, parent2)
        if random.random() < mutation_rate:
            child = mutate(child)
        new_population.append(child)
        
    population = new_population

# Re-evaluate final population to ensure indices match
final_fitness_scores = [evaluate_fitness(schedule) for schedule in population]
best_schedule = population[final_fitness_scores.index(min(final_fitness_scores))]

print("\nBest Schedule (Staff x Shifts):")
for staff in range(num_staff):
    print(f"Staff {staff + 1} (Total Shifts: {sum(best_schedule[staff])}): {best_schedule[staff]}")