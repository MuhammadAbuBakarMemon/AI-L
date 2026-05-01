# QUESTION

# Problem:
# You are given three variables x, y, and z, each of which can take integer values from 0 to 2 (inclusive).
# The constraint is:
# x must not be equal to y
# Your task is to:
# Find all possible valid assignments of x, y, and z that satisfy the constraint.
# Print every solution as it is found.
# Count the total number of valid solutions.

# Real-world style version:
# Three devices (x, y, z) can each be assigned a channel from 0 to 2. Devices x and y cannot use the same channel due to interference.
# Find all valid channel assignments and report how many such assignments exist.

from ortools.sat.python import cp_model

class VarArraySolutionPrinter(cp_model.CpSolverSolutionCallback):

    """print intermediate solutions"""

    def __init__(self, variables : list[cp_model.IntVar]):
        # cp_model.CpSolverSolutionCallback(self) manul class call is incorrect 
#weren't actually "initializing" the parent part of your object. Instead, you were trying to call the class definition itself as if it were a function, 
# passing self into it.
# Because CpSolverSolutionCallback is a specialized class (written in C++ and wrapped in Python), it requires a very specific setup. When you don't use 
# super().__init__(), the internal C++ "engine" of the solver doesn't get linked to your Python object. This leads to the TypeError you saw: Python 
# essentially says, "You're trying to use a blueprint (the class) as a tool (the instance), and I don't know how to handle that."
        super().__init__()
        self.__variables = variables
        self.__solution_count = 0

    def on_solution_callback(self) -> None:
        self.__solution_count += 1

        for v in self.__variables:
            # print(f"P{v} = {self.value(v)}", end = " ")
            # self.Value(v): The OR-Tools library uses PascalCase for its solver methods (like Value, Solve, Add). If you use lowercase value, 
            # Python will throw an AttributeError.
            print(f"{v} = {self.Value(v)}")
        print()

    @property
    def solution_count(self):
         return self.__solution_count

def search_for_all_solutions_sample_sat():
    
    """Showcases calling the solver to search for all solutions."""

    model = cp_model.CpModel()

    num_vals = 3

    x = model.NewIntVar(0, num_vals - 1, "x")
    y = model.NewIntVar(0, num_vals - 1, "y")
    z = model.NewIntVar(0, num_vals - 1, "z")

    model.add(x != y)
    
    solver = cp_model.CpSolver()

    solution_printer = VarArraySolutionPrinter([x, y, z])
    solver.parameters.enumerate_all_solutions = True
    status = solver.solve(model, solution_printer)

    print(f"Status = {solver.status_name(status)}")
    print(f"Number of solutions founnd: {solution_printer.solution_count}")

search_for_all_solutions_sample_sat()    

# RECALL

# Ultra-short Recall (exam panic version)
# Say this in your head:

# Class → store vars → count → print each solution
# Model → variables → constraint
# Printer → enable all solutions → solve with printer → print count

