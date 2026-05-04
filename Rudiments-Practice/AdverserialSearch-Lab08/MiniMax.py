import math

class Node:

    def __init__(self, value=None):
        self.value = value
        self.minmax_value = None
        self.children = []

class MinimaxAgent: 

    def __init__(self, depth):
        self.depth = depth

    def formulate_goal(self, node):
        return "Goal Reached" if node.minmax_value is not None else "Searching"
    
    def act(self, node, environment):

        goal_status = self.formulate_goal(node)
        if goal_status == "Goal Reached":
            return f"Minmax value for root node is: {node.minmax_value}"
        else:
            return environment.compute_minmax(node, self.depth, True)

class Environment:
        
    def __init__(self, tree):
        self.tree = tree
        self.computed_nodes = []

    def get_percept(self, node):
        return node
    
    def compute_minmax(self, node, depth, maximizingPlayer = True):
        if depth == 0 or not node.children:
            node.minmax_value = node.value
            self.computed_nodes.append(node.value)
            return node.value
        
        if maximizingPlayer:
            value = - math.inf
            for child in node.children:
                child_value = self.compute_minmax(child, depth - 1, False)
                value = max(value, child_value)
            node.minmax_value = value
            self.computed_nodes.append(node.value)
            return value
        else:
            value = math.inf
            for child in node.children:
                child_value = self.compute_minmax(child, depth - 1, True)
                value = min(value, child_value)
            node.minmax_value = value
            self.computed_nodes.append(node.value)
            return value

def run_agent(agent, environment, start_node):
    percept = environment.get_percept(start_node)
    agent.act(percept, environment)


# --- Sample Tree Setup ---
root = Node("A")
n1 = Node("B")
n2 = Node("C")
root.children = [n1, n2]

n3 = Node("D")
n4 = Node("E")
n1.children = [n3, n4]

n5 = Node("F")
n6 = Node("G")
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

# --- Execution ---
depth = 3
agent = MinimaxAgent(depth)
environment = Environment(root)
run_agent(agent, environment, root)

print("Computed Nodes: ", environment.computed_nodes)
print("Minimax Values: ")

print("A: ", root.minmax_value)
print("B: ", n1.minmax_value)
print("C: ", n2.minmax_value)
print("D: ", n3.minmax_value)
print("E: ", n4.minmax_value)
print("F: ", n5.minmax_value)
print("G: ", n6.minmax_value)
