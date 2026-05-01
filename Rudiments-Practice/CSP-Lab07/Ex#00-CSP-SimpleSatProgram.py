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
    x = model.new_int_var(0, num_vals - 1, "x")
    y = model.new_int_var(0, num_vals - 1, "y")
    z = model.new_int_var(0, num_vals - 1, "z")

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