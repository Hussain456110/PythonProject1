class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node, neighbor, cost=1):
        if node not in self.graph:
            self.graph[node] = []
        self.graph[node].append((neighbor, cost))

    # Uniform Cost Search (UCS)
    def ucs(self, start, goal):
        visited = set()
        queue = [(0, start, [])]  # (cost, node, path)

        while queue:
            queue.sort()  # Sort queue based on cost
            cost, node, path = queue.pop(0)
            if node in visited:
                continue
            visited.add(node)
            path=path+[node]

            if node == goal:
                return path, cost

            for neighbor, step_cost in self.graph.get(node, []):
                if neighbor not in visited:
                    queue.append((cost + step_cost, neighbor, path))

        return None

# Example usage:
graph = Graph()
edges = [
    ('A', 'B', 1), ('A', 'C', 2), ('B', 'D', 4), ('C', 'D', 1),
    ('B', 'E', 1), ('D', 'F', 3), ('E', 'F', 2)
]

for edge in edges:
    graph.add_edge(*edge)
print(graph.graph)
print("UCS:", graph.ucs('A', 'F'))
