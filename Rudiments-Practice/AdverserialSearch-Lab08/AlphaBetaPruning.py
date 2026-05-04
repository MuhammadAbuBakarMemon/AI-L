import math 

class Node:

    def __init__(self, value = None):
        self.value = value
        self.children = []
        self.minmax_value = None

class MinimaxAgent:

    def __init__(self, depth):
        self.depth = depth

    def formulate_goal(self, node):
        return "Goal Reached" if node.minmax_value is not None else "Searching"

    def act(self, environment, node):

        goal_status = self.formulate_goal(node)
        if goal_status == "Goal Reached":
            return f"Minmax value for root: {node.minmax_value}"
        else:
            return environment.alpha_beta_search(node, self.depth, -math.inf, math.inf, True)

class Environment:

    def __init__(self, tree):
        self.tree = tree
        self.computed_nodes = []

    def get_percept(self, node):
        return node

    def alpha_beta_search(self, node, depth, alpha, beta, maximizingPlayer = True):

        if depth == 0 or not node.children:
            node.minmax_value = node.value
            self.computed_nodes.append(node.value)
            return node.value 
        
        if maximizingPlayer:
            value = -math.inf
            for child in node.children:
                child_value = self.alpha_beta_search(child, depth - 1, alpha, beta, False)
                value = max(value, child_value)
                alpha = max(alpha, value)
                if alpha >= beta:
                    print(f"Pruning remaining children of node: '{node.value}' (triggered by evaluating) {child.value}")
                    break
            self.computed_nodes.append(node.value)
            node.minmax_value = value 
            return value
        else:
            value = math.inf
            for child in node.children:
                child_value = self.alpha_beta_search(child, depth - 1, alpha, beta, True)
                value = min(child_value, value)
                beta = min(beta, value)
                if alpha >= beta:
                    print(f"Pruning remainig children of node: '{node.value}' (Triggered by {child.value})")
                    break 
            self.computed_nodes.append(node.value)
            node.minmax_value = value
            return value
        
def run_agent(agent, environment, start_node):
    percept = environment.get_percept(start_node)
    agent.act(environment, percept)


root = Node('A')
n1 = Node('B')
n2 = Node('C')
root.children = [n1, n2]

n3 = Node('D')
n4 = Node('E')
n5 = Node('F')
n6 = Node('G')
n1.children = [n3, n4]
n2.children = [n5, n6]

n7 = Node(2)
n8 = Node(3)
n9 = Node(5)
n10 = Node(9)
n3.children = [n7, n8]
n4.children = [n9, n10]

n11 = Node(0)
n12 = Node(1)
n13 = Node(7)
n14 = Node(5)
n5.children = [n11, n12]
n6.children = [n13, n14]

depth = 3
agent = MinimaxAgent(depth)
environment = Environment(root)
run_agent(agent, environment, root)

print("\n--- Results ---")
print("Computed Nodes sequence:", environment.computed_nodes)
print("\nMinimax values assigned to intermediate nodes:")
print(f"A: {root.minmax_value}")
print(f"B: {n1.minmax_value}")
print(f"C: {n2.minmax_value}")
print(f"D: {n3.minmax_value}")
print(f"E: {n4.minmax_value}")
print(f"F: {n5.minmax_value}")
print(f"G: {n6.minmax_value}")
print(f"\nFinal Minimax value for root node: {root.minmax_value}")

