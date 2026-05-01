# QUESTION

# Problem: The 8-Queens Puzzle
# You are given a standard 8 × 8 chessboard.

# Your task is to:
# Place 8 queens on the board such that:
# No two queens are in the same row
# No two queens are in the same column
# No two queens are on the same diagonal
# Find all possible valid arrangements of the 8 queens.
# For each valid solution:
# Display the board using:
# Q for a queen
# _ for an empty space

# Objective:
# Enumerate every valid configuration where no queen attacks another.


from ortools.sat.python import cp_model

model = cp_model.CpModel()

board_size = 8

queens = [model.NewIntVar(0, board_size - 1, f"x_{x}") for x in range(board_size)]

# all queens placed on different rows
model.AddAllDifferent(queens)

# now we check for diagonal placement of queens such that tehy don't attack
# a trick 
# queens placed in diagonals follow this rule 
# FOR 1 DIAGONAL 
# row + column = constant  
# FOR THE OTHER DIAGONAL 
# row - column = constant

# so of 2 queens share the same diagonal then these constants become similar, and this AddAllDifferent() function then ensures that this doesn't happens  
model.AddAllDifferent(queens[x] + x for x in range(board_size))
model.AddAllDifferent(queens[x] - x for x in range(board_size))

#extra diagonal modelling redundant but useful for educational purposes, 
#my code can still work without this, 
#try commenting it out and see for yourselves

diag1 = []

for x in range(board_size):
    q1 = model.NewIntVar(0, 2 * board_size, f"diag1_{x}")
    diag1.append(q1)
    model.add(q1 == queens[x] + x)

model.AddAllDifferent(diag1)

#this part just enforces constraints differently

class NQueensSolutionPrinter(cp_model.CpSolverSolutionCallback):
    """Print intermediate solutions."""

    def __init__(self, queens : list[cp_model.IntVar]):
        super().__init__()
        self.__queens = queens
        self.__solution_count = 0

    def on_solution_callback(self):
        self.__solution_count += 1
        for x in range(board_size):
            rows = self.Value(self.__queens[x])

            for y in range(board_size):
                if rows == y:
                    print("Q", end = " ")
                else:
                    print("_", end = " ")
            print()
        print()
        
solver = cp_model.CpSolver()
solution_printer = NQueensSolutionPrinter(queens)
solver.parameters.enumerate_all_solutions = True
status = solver.solve(model, solution_printer )

