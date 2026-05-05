def best_first_scheduling():
    # 1. Exact data from the exam paper
    heuristics = {"T0": 5, "T1": 3, "T2": 4, "T3": 2, "T4": 1, "T5": 2, "T6": 0}
    
    # Corrected: Dictionary of dictionaries 
    graph = {
        "T0": {"T1": 1, "T2": 1},
        "T1": {"T3": 1, "T4": 1},
        "T2": {"T5": 1},
        "T3": {"T6": 1},
        "T4": {"T6": 1},
        "T5": {"T6": 1},
        "T6": {}
    }
    
    # 2. Count dependencies (in-degrees)
    dependencies = {node: 0 for node in heuristics}
    for task, successors_dict in graph.items():
        # Because successors_dict is a dictionary like {"T1": 1, "T2": 1}, 
        # looping through it grabs just the keys ("T1", "T2")
        for successor in successors_dict:
            dependencies[successor] += 1
            
    # 3. Find starting tasks (0 dependencies)
    available_tasks = [(heuristics[task], task) for task in dependencies if dependencies[task] == 0]
    
    execution_sequence = []
    
    # 4. Process tasks
    while available_tasks:
        # Sort by lowest heuristic (Best-First)
        available_tasks.sort(key=lambda x: x[0])
        
        current_h, current_task = available_tasks.pop(0)
        execution_sequence.append(current_task)
        
        # Look at the dictionary of tasks that depended on the one we just finished
        for successor in graph[current_task]:
            dependencies[successor] -= 1 # Remove one lock
            
            if dependencies[successor] == 0:
                available_tasks.append((heuristics[successor], successor))
                
    return execution_sequence

final_order = best_first_scheduling()
print(f"Final Execution Sequence: {final_order}")