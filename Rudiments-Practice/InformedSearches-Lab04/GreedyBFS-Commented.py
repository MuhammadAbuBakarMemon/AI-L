# Graph with different edge costs
graph = {
    'A': {'B': 2, 'C': 1},
    'B': {'D': 4, 'E': 3},
    'C': {'F': 1, 'G': 5},
    'D': {'H': 2},
    'E': {},
    'F': {'I': 6},
    'G': {},
    'H': {},
    'I': {}
}

# Heuristic function (estimated cost to reach goal 'I')
heuristic = {
    'A': 7, 'B': 6, 'C': 5, 'D': 4, 'E': 7, 'F': 3, 'G': 6, 'H': 2, 'I': 0
}

# Greedy Best-First Search Function (without heapq)
def greedy_bfs(graph, start, goal):
    
    # FIXED: Moved "(sorted manually)" into the comment line above
    frontier = [(start, heuristic[start])] # List-based priority queue (sorted manually)
    
    visited = set() # Set to keep track of visited nodes
    came_from = {start: None} # Path reconstruction
    
    # FIXED: Indented the entire function body properly
    while frontier:
        # Sort frontier manually by heuristic value (ascending order)
        frontier.sort(key=lambda x: x[1])
        
        current_node, _ = frontier.pop(0) # Get node with best heuristic
        
        if current_node in visited:
            continue
            
        print(current_node, end=" ") # Print visited node
        visited.add(current_node)
        
        # If goal is reached, reconstruct path
        if current_node == goal:
            path = []
            # FIXED: Used a separate variable 'curr' to walk backward through the path
            curr = current_node 
            while curr is not None:
                path.append(curr)
                curr = came_from[curr]
            path.reverse()
            print(f"\nGoal found with GBFS. Path: {path}")
            return
            
        # Expand neighbors based on heuristic
        for neighbor in graph[current_node]:
            # FIXED: Added a check to prevent overwriting paths for nodes already in the frontier
            in_frontier = any(neighbor == n[0] for n in frontier)
            
            if neighbor not in visited and not in_frontier:
                came_from[neighbor] = current_node
                frontier.append((neighbor, heuristic[neighbor]))
                
    print("\nGoal not found")

# Run Greedy Best-First Search
print("Following is the Greedy Best-First Search (GBFS):")
greedy_bfs(graph, 'A', 'I')