# QUESTION
# You have three variables x, y, and z, each of which can take an integer value from 0 to 2 (inclusive).
# The only restriction is:
# # x must not be equal to y
# There are no restrictions on z.
# Find any valid assignment of values to x, y, and z that satisfies the constraint.

"""Simple Solve"""

from ortools.sat.python import cp_model

def simple_sat_program():

    model = cp_model.CpModel()
    
    num_vals = 3
    x = model.NewIntVar(0, num_vals - 1, "x")
    y = model.NewIntVar(0, num_vals - 1, "y")
    z = model.NewIntVar(0, num_vals - 1, "z")

    model.add(x != y)

    solver = cp_model.CpSolver()
    status = solver.solve(model)

    if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
        print(f"x = {solver.value(x)}")
        print(f"y = {solver.value(y)}")
        print(f"z = {solver.value(z)}")
    else:
        print("No solution found!!!")

simple_sat_program()

# BELOW IS ME ABSUING MY AI AGENT

# memorizing all this code is very difficult give me some steps to memorize that describle the flow of this code that when and if i sit in an exam to write 
# all such stuff and I just happen to forget this then I can easily recall the line/part of code I am missing by recalling these line that describe the work 
# flow for my program

# Ultra-short recall version (exam panic mode)
# Just remember this sentence:
# Model → Variables → Constraints → Solver → Solve → Show