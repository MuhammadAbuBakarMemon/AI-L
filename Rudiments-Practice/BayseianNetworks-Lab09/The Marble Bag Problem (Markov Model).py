# Import the NumPy library and alias it as 'np'. This provides powerful array operations and random selection tools.
import numpy as np

# Define a list containing the names of the two possible states in our Markov system.
states = ["Red", "Blue"]

# Create a 2D NumPy array representing the transition probability matrix.
transition_matrix = np.array([
    # Row index 0 (From "Red"): 50% chance to stay "Red", 50% chance to transition to "Blue".
    [0.5, 0.5], 
    # Row index 1 (From "Blue"): 50% chance to transition to "Red", 50% chance to stay "Blue".
    [0.5, 0.5]  
])

# Define a function to simulate the Markov chain. It requires a starting state and the number of transitions to run.
def simulate_markov_process(initial_state, num_steps):
    # Set the current state of the simulation to the provided starting state.
    current_state = initial_state
    
    # Initialize a list to keep a history of all visited states, starting with the first one.
    state_sequence = [current_state]
    
    # Start a loop that will repeat for the specified 'num_steps'. The '_' is a placeholder for the loop counter, as we don't need its value.
    for _ in range(num_steps):
        # Check if the current state is "Red".
        if current_state == "Red":
            # Randomly pick the next state from the 'states' list, using the probabilities from the first row of our matrix.
            next_state = np.random.choice(states, p=transition_matrix[0])
        # If the state is not "Red", it must be "Blue".
        else:
            # Randomly pick the next state from the 'states' list, using the probabilities from the second row of our matrix.
            next_state = np.random.choice(states, p=transition_matrix[1])
            
        # Add the newly chosen state to our historical sequence list.
        state_sequence.append(next_state)
        
        # Update the current state to be the newly chosen state, preparing for the next loop iteration.
        current_state = next_state
        
    # After the loop finishes, return the full list of states visited.
    return state_sequence

# Define the starting parameter for the simulation as "Red".
initial_state = "Red"

# Define how many state transitions we want to simulate (10 steps).
num_steps = 10

# Execute the simulation function with our parameters and store the resulting list in the 'state_sequence' variable.
state_sequence = simulate_markov_process(initial_state, num_steps)

# Print a formatted introductory sentence detailing the parameters of the simulation we just ran.
print(f"State sequence for {num_steps} steps starting from {initial_state}:")

# Take the list of state strings, join them together into a single string separated by " -> ", and print it to the console.
print(" -> ".join(state_sequence))