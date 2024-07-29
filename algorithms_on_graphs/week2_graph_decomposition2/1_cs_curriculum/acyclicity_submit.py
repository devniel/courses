# Uses python3

import sys


def dfs_explore(v, adj, visited_dict, recursion_stack):
    # Mark current node as visited
    visited_dict[v] = True
    # Add it to recursion stack
    recursion_stack[v] = True

    # Check all neighbours
    for neighbour in adj[v]:
        # If neighbour is already in recursion stack, then it's a back edge between
        # v and neighbour
        if not visited_dict[neighbour]:
            has_cycle = dfs_explore(neighbour, adj, visited_dict, recursion_stack)
            if has_cycle:
                return True
        elif recursion_stack[neighbour]:
            return True

    # Remove node from recursion stack
    recursion_stack[v] = False
    return False


def dfs(adjacent_list):
    visited = [None] * len(adjacent_list)
    recursion_stack = [None] * len(adjacent_list)

    for vertex in range(0, len(adjacent_list)):
        visited[vertex] = False
        recursion_stack[vertex] = False

    for vertex in range(0, len(adjacent_list)):
        if not visited[vertex]:
            has_cycle = dfs_explore(vertex, adj, visited, recursion_stack)
            if has_cycle:
                return True
        elif recursion_stack[vertex]:
            return True

    return False


def acyclic(adjacent_list):
    return int(dfs(adjacent_list))


if __name__ == '__main__':
    input = "\n".join(sys.stdin.readlines())
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))
