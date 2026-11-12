
def graph_program():

    graph = {
        "S": ["E", "B"],
        "E": ["S", "I", "A"],
        "B": ["S", "A", "L"],
        "I": ["E", "A"],
        "A": ["E", "I", "B"],
        "L": ["B"]
    }

    # BFS
    def bfs(start):
        visited = []
        queue = [start]

        while queue:
            node = queue.pop(0)

            if node not in visited:
                visited.append(node)

                for neighbor in graph[node]:
                    if neighbor not in visited and neighbor not in queue:
                        queue.append(neighbor)

        return visited

    # DFS
    def dfs(start, visited=None):
        if visited is None:
            visited = []

        visited.append(start)

        for neighbor in graph[start]:
            if neighbor not in visited:
                dfs(neighbor, visited)

        return visited

    print("BFS:", bfs("S"))
    print("DFS:", dfs("S"))
