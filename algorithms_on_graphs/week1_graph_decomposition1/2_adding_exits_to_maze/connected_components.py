#Uses python3

import sys


def explore(v, adjacent_list, visited_dict=None):
    if visited_dict is None:
        visited_dict = {}
    else:
        visited_dict = visited_dict.copy()
    print(f"explore: {v}")
    print(f"neighbours: {adjacent_list[v]}")
    visited_dict[v] = True
    for neighbour in adjacent_list[v]:
        if neighbour not in visited_dict:
            visited_dict = explore(neighbour, adjacent_list, visited_dict)
    return visited_dict


def number_of_components(adjacent_list):
    connected_components_counter = 0
    visited_dict = {}
    for v in range(0, len(adjacent_list)):
        print(f"Checking vertex {v}")
        if v not in visited_dict:
            visited_dict = explore(v, adjacent_list, visited_dict)
            print(f"Updated visited dict {visited_dict}")
            connected_components_counter = connected_components_counter + 1
    return connected_components_counter


if __name__ == '__main__':
    input = "\n".join(sys.stdin.readlines())
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(adj)
    print(number_of_components(adj))
