import sys
import string

class Graph:

    def __init__(self, number_nodes, edges):
        # We make a Graph object and its adjacency list
        self.adjacency = []
        for _ in range(number_nodes + 1):
            self.adjacency.append([])
        # Which will have an array with all the edges from the input
        for (s, d) in edges:
            self.adjacency[s].append(d)
            self.adjacency[d].append(s)

        # Using the adjacents in the Graph we make another array
        self.adjacency_len = [None] * (number_nodes + 1)
        for i in range(len(self.adjacency)):
            self.adjacency_len[i] = len(self.adjacency[i])
        # The next line will rank the nodes in the way that the algorithm must iterate through them
        self.order = sorted(range(len(self.adjacency_len)), key=lambda k: (self.adjacency_len[k], -k), reverse=True)
        # Pop the last element from the list, which is 0
        self.order.pop()
        # This list will have the correct order of the nodes

def graphColour(graph):
    # Make a dictionary for the nodes and their colours
    nodes_colours = {}

    # Iterate through each node in the Graph, in the specified order
    for u in graph.order:
        current_colours = set()

        # For loop to check for already assigned colours
        for i in graph.adjacency[u]:
            if i in nodes_colours:
                current_colours.add(nodes_colours.get(i))

        # Search for the first free colour
        selected_colour = 0
        for colour in current_colours:
            if selected_colour is not colour:
                break
            selected_colour = selected_colour + 1

        # Assing the selected colour to the corresponding node
        # In the used colours dictionary
        nodes_colours[u] = selected_colour
 
    # Print colours
    # for v in range(number_nodes):
    #     print("{}{}".format(v + 1, colours[nodes_colours[v + 1]]))

    return nodes_colours


input_file = sys.argv[1]
output_file = sys.argv[2]
# Read input file and assign it in a list
with open(input_file) as f:
    lines = f.readlines()
lines = [x.strip() for x in lines]
# Rearange list and split for preferred usage
for i in range(len(lines)):
    lines[i] = lines[i][2:]
    lines[i] = lines[i].split()

# Initiate variables
colours = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
number_nodes = len(lines)
edges = []
# Change lines list into an edges list
for i in range(len(lines)):
    for j in range(len(lines[i])):
        edges.append((i+1, int(lines[i][j])))

# Create the graph object
graph = Graph(number_nodes, edges)
# Call the graph colouring algorithm for the specific graph
nodes_colours = graphColour(graph)

# Output result into a txt file
with open(output_file, 'w') as f:
    sys.stdout = f
    for v in range(number_nodes):
        # If statement to get rid of the trailing newline at the end of the txt file
        # if v == len(range(number_nodes))-1:
        #     print("{}{}".format(v + 1, colours[nodes_colours[v + 1]]), file = f, end='')
        #     break
        print("{}{}".format(v + 1, colours[nodes_colours[v + 1]]), file = f)
        