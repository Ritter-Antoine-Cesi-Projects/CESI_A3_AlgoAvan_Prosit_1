import time

graph = {
    'A': [0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    'B': [1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    'C': [1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    'D': [0, 0, 1, 0, 1, 0, 1, 0, 0, 0],
    'E': [0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
    'F': [0, 0, 0, 0, 1, 0, 1, 0, 1, 0],
    'G': [0, 0, 0, 1, 0, 1, 0, 1, 0, 1],
    'H': [0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
    'I': [0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    'J': [0, 0, 0, 0, 0, 0, 1, 0, 1, 0]
}

def is_eulerian(graph):
    for node in graph:
        if sum(graph[node]) % 2 != 0:
            return False
    return True

def find_eulerian_path(graph, start):
    if not is_eulerian(graph):
        return "Le graphe n'est pas eulerien"
    path = []
    def find_path(node):
        for i, neighbor in enumerate(graph[node]):
            if neighbor > 0:
                graph[node][i] -= 1
                graph[list(graph.keys())[i]][list(graph.keys()).index(node)] -= 1
                find_path(list(graph.keys())[i])
        path.append(node)
    find_path(start)
    return path

start_point = 'I'
start = time.time()
path = find_eulerian_path(graph, start_point)
end = time.time()
print(path)
print("Temps d'exécution : ", end - start, "s")