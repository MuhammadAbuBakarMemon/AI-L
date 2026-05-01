# QUESTION 

# A company produces three products represented by variables x, y, and z. The production of these products is limited by available resources.

# Each unit of product uses resources as follows:

# Constraint 1 (Resource A):
# 2x+7y+3z≤50
# Constraint 2 (Resource B):
# 3x−5y+7z≤45
# Constraint 3 (Resource C):
# 5x+2y−6z≤37

# All variables must be non-negative integers.
# Objective:
# Maximize the total profit given by:
# Profit=2x+2y+3z

from ortools.sat.python import cp_model

def main():

    """Minimal CP-SAT example to showcase calling the solver."""

    model = cp_model.CpModel()

    var_upper_bound = max(50, 45, 37)

    x = model.NewIntVar(0, var_upper_bound, "x")
    y = model.NewIntVar(0, var_upper_bound, "y")
    z = model.NewIntVar(0, var_upper_bound, "z")    

    model.add(2 * x + 7 * y + 3 * z <= 50)
    model.add(3 * x - 5 * y + 7 * z <= 45)
    model.add(5 * x + 2 * y - 6 * z <= 37)

    model.maximize(2 * x + 2 * y + 3 * z)
    #for setting up the OBJECTIVE FUNCTION - model.maximize()
    #for obtaining the maximum value from the objective function - solver.objective_value

    solver = cp_model.CpSolver()
    status = solver.solve(model)

    if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
        print(f"Maximum value of Objective function: {solver.objective_value}\n")
        print(f"x = {solver.Value(x)}")
        print(f"y = {solver.Value(y)}")
        print(f"z = {solver.Value(z)}")
    else:
        print("Solution not found/////")

    print("\nStatistics")
    print(f" Status: {solver.status_name(status)}")
    print(f" Conflicts: {solver.num_conflicts}")
    print(f" Branches: {solver.num_branches}")
    print(f" Wall Time: {solver.wall_time}s")

if __name__ == "__main__":
    main()