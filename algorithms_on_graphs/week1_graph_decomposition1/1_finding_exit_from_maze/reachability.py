import sys


def explore(v, adj, visited_dict={}):
    print(f"explore: {v}")
    print(f"neighbours: {adj[v]}")
    visited_dict[v] = True
    for neighbour in adj[v]:
        if neighbour not in visited_dict:
            explore(neighbour, adj)
    return visited_dict


def reach(adj, x, y):
    print(f"reach? {x} {y}")
    visited_dict = explore(x, adj)
    print(f"visited_dict: {visited_dict}")
    return int(y in visited_dict)


if __name__ == '__main__':
    input = "\n".join(sys.stdin.readlines())
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    x, y = data[2 * m:]
    adj = [[] for _ in range(n)]
    x, y = x - 1, y - 1
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    is_reachable = reach(adj, x, y)
    print("------")
    print(is_reachable)
