# Graph with different edge costs
graph = {
    'A': {'B': 4, 'C': 3},
    'B': {'E': 12, 'F': 5},
    'C': {'D': 7, 'E': 10},
    'D': {'E': 2},
    'E': {'G': 5},
    'F': {'G': 16},
    'G': {},
}

# Heuristic values for A* search
heuristic = {
    'A': 14, 
    'B': 12, 
    'C': 11, 
    'D': 6, 
    'E': 4, 
    'F': 11, 
    'G': 0 
}

def a_star(graph, start, goal):
    frontier = [(start, 0 + heuristic[start])] # List-based priority queue (sorted manually)
    visited = set() # Set to keep track of visited nodes
    g_costs = {start: 0} # Cost to reach each node from start
    came_from = {start: None} # Path reconstruction
    
    while frontier:
        # Sort frontier by f(n) = g(n) + h(n)
        frontier.sort(key=lambda x: x[1])
        current_node, current_f = frontier.pop(0) # Get node with lowest f(n)
        
        if current_node in visited:
            continue
            
        print(current_node, end=" ") # Print visited node
        visited.add(current_node)
        
        # If goal is reached, reconstruct path
        if current_node == goal:
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = came_from[current_node]
            path.reverse()
            print(f"\nGoal found with A*. Path: {path}")
            return
            
        # Explore neighbors
        for neighbor, cost in graph[current_node].items():
            new_g_cost = g_costs[current_node] + cost # Path cost from start to neighbor
            f_cost = new_g_cost + heuristic[neighbor] # f(n) = g(n) + h(n)
            
            # Update path if neighbor is unvisited or we found a shorter path
            if neighbor not in g_costs or new_g_cost < g_costs[neighbor]:
                g_costs[neighbor] = new_g_cost
                came_from[neighbor] = current_node
                frontier.append((neighbor, f_cost))

    print("\nGoal not found")

# Run A* Search
print("Following is the A* Search:")
a_star(graph, 'A', 'G')