def dfs(v, adj, order, visited, visiting):
    if v in visiting:
        raise ValueError("Graph has at least ony cycle, topological sort not possible")
    if v not in visited:
        visiting.add(v)
        for neighbor in adj[v]:
            dfs(neighbor, adj, order, visited, visiting)
        visiting.remove(v)
        visited.add(v)
        order.append(v)

def topological_sort_dfs(graph):
    visited = set()
    visiting = set()
    order = []

    for v in graph:
        if v not in visited:
            dfs(v, graph, order, visited, visiting)

    return order[::-1]


if __name__ == "__main__":
    graph = {
        1: [],
        2: [],
        3: [1],
        4: []
    }
    topo_sort = topological_sort_dfs(graph)
    print(topo_sort)
