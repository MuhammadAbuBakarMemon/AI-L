def solve_cleaning_robot():
    # Representing the 4x5 grid exactly as shown in the exam paper
    # 'S' = Start, 'X' = Obstacle, numbers = cleanliness score
    grid = [
        ['S', '2', '0', '0', '1'],
        ['0', 'X', '1', '2', '0'],
        ['0', '2', '0', 'X', '0'],
        ['0', '0', '1', '0', '2']
    ]
    
    rows = len(grid)
    cols = len(grid[0])
    max_moves = 8
    
    # Start position (S is at 0,0)
    start_r, start_c = 0, 0
    
    # Possible movements: (row_change, col_change, Action_Name)
    directions = [(-1, 0, 'Up'), (1, 0, 'Down'), (0, -1, 'Left'), (0, 1, 'Right')]
    
    best_score = -1
    best_path = []
    best_actions = []
    
    # Helper function to convert grid string values to integers
    def get_value(r, c):
        val = grid[r][c]
        if val in ('S', '0', 'X'): 
            return 0
        return int(val)

    # DFS function to explore all paths
    def dfs(r, c, moves_left, current_score, cleaned_cells, path, actions):
        nonlocal best_score, best_path, best_actions
        
        # Update the best score if the current path is better
        if current_score > best_score:
            best_score = current_score
            best_path = list(path)
            best_actions = list(actions)
            
        # Stop exploring this branch if we are out of moves (energy)
        if moves_left == 0:
            return
        
        # Explore all valid neighboring cells
        for dr, dc, action_name in directions:
            nr, nc = r + dr, c + dc
            
            # Check boundaries and ensure we don't hit an obstacle ('X')
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != 'X':
                
                # Check if the cell has already been cleaned in this specific path
                cell_val = get_value(nr, nc)
                earned_score = cell_val if (nr, nc) not in cleaned_cells else 0
                
                # Mark cell as cleaned for future moves in this branch
                new_cleaned = cleaned_cells.copy()
                new_cleaned.add((nr, nc))
                
                # Track the path and actions
                path.append((nr, nc))
                actions.append(action_name)
                
                # Move to the next cell recursively
                dfs(nr, nc, moves_left - 1, current_score + earned_score, new_cleaned, path, actions)
                
                # Backtrack (undo the move to explore other branches)
                path.pop()
                actions.pop()

    # Initialize the search
    initial_cleaned = {(start_r, start_c)} # Mark starting cell as visited/cleaned
    initial_path = [(start_r, start_c)]
    
    # Start the recursive search
    dfs(start_r, start_c, max_moves, 0, initial_cleaned, initial_path, [])
    
    return best_score, best_path, best_actions

# Run the algorithm and display the results
score, path, actions = solve_cleaning_robot()

print("--- Utility-Based Agent Simulation ---")
print(f"Maximum Cleanliness Score: {score}")
print(f"Sequence of Actions: {actions}")
print("Path Coordinates (row, col):")
for step, coords in enumerate(path):
    if step == 0:
        print(f"Start: {coords}")
    else:
        print(f"Move {step}: {coords} ({actions[step-1]})")