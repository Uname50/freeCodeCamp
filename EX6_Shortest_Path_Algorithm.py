# This exercise is aimed at practicing algorithm design 

# Notes:

# Graphs are data structures representing relations between pairs of elements. These elements, called nodes, can be real-life objects, entities, points in space or others. 
#The connections between the nodes are called the edges. For example, a graph can be used to represent two points in the space, A and B, connected by a path. A graph like this will be made of two nodes connected by an edge.

# A graph is called a weighted graph when its edges are associated with weights, representing a distance, time or other quantitative value.

# for node in graph:
#     unvisited.append(node)
#     if node == start:
#         distances[node] = 0
#     else:
#         distances[node] = float('inf')
# print(f'Unvisited: {unvisited}\nDistances: {distances}')

# The list() type constructor enables you to build a list from an iterable.

# With a dictionary comprehension, you can create a dictionary starting from an existing dictionary:
# {key: val for key in dict} 

# Dictionary comprehensions support conditional if/else syntax as well:
# {key: val_1 if condition else val_2 for key in dict}

my_graph = {
    'A': [('B', 5), ('C', 3), ('E', 11)],
    'B': [('A', 5), ('C', 1), ('F', 2)],
    'C': [('A', 3), ('B', 1), ('D', 1), ('E', 5)],
    'D': [('C',1 ), ('E', 9), ('F', 3)],
    'E': [('A', 11), ('C', 5), ('D', 9)],
    'F': [('B', 2), ('D', 3)]
}

def shortest_path(graph, start, target = ''):
    unvisited = list(graph)
    distances = {node: 0 if node == start else float('inf') for node in graph}
    paths = {node: [] for node in graph}
    paths[start].append(start)
    
    while unvisited:
        current = min(unvisited, key=distances.get)
        for node, distance in graph[current]:
            if distance + distances[current] < distances[node]:
                distances[node] = distance + distances[current]
                if paths[node] and paths[node][-1] == node:
                    paths[node] = paths[current][:]
                else:
                    paths[node].extend(paths[current])
                paths[node].append(node)
        unvisited.remove(current)
    
    targets_to_print = [target] if target else graph
    for node in targets_to_print:
        if node == start:
            continue
        print(f'\n{start}-{node} distance: {distances[node]}\nPath: {" -> ".join(paths[node])}')
    
    return distances, paths
    
shortest_path(my_graph, 'A')