#Uses python3

import sys

sys.setrecursionlimit(200000)


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Split the array in two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Sort the array recursively
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    # Merge the sorted halves
    return merge(left_sorted, right_sorted)

def merge(left, right):
    sorted_array = []
    left_index, right_index = 0, 0

    # Merge both sidex while there are elements on them
    while left_index < len(left) and right_index < len(right):
        if left[left_index]["end_time"] is None:
            sorted_array.insert(0, left[left_index])
            left_index += 1
        elif right[right_index]["end_time"] is None:
            sorted_array.insert(0, right[right_index])
            right_index += 1
        elif left[left_index]["end_time"] > right[right_index]["end_time"]:
            sorted_array.append(left[left_index])
            left_index += 1
        else:
            sorted_array.append(right[right_index])
            right_index += 1

    # Add remaining elements to its half
    sorted_array.extend(left[left_index:])
    sorted_array.extend(right[right_index:])

    return sorted_array

def dfs(v, adj, registry, time):
    time[0] += 1
    registry[v]["status"] = 1
    registry[v]["start_time"] = time[0]

    for neighbor in adj[v]:
        if registry[neighbor]["status"] == 0:
            dfs(neighbor, adj, registry, time)

    time[0] += 1
    registry[v]["status"] = 2
    registry[v]["end_time"] = time[0]


def dfs2(v, adj, visited, tree):
    visited[v] = 1
    tree.append(v)
    for neighbor in adj[v]:
        if visited[neighbor] == 0:
            dfs2(neighbor, adj, visited, tree)
    return tree

def get_inversed_adj(adj):
    inverted = [[] for _ in range(0, len(adj))]

    for v in range(0, len(adj)):
        for j in adj[v]:
            inverted[j].append(v)

    return inverted

def number_of_strongly_connected_components(adj):

    # Create registry with finishing times per vertex
    registry = []
    for i in range(0, len(adj)):
        registry.append({
            "status": 0,
            "start_time": None,
            "end_time": None,
            "vertex": i
        })

    time = [0]

    for i in range(0, len(adj)):
        if registry[i]["status"] == 0:
            dfs(i, adj, registry, time)

    # Get vertex sorted by the finishing times
    sorted_registry = merge_sort(registry)
    sorted_adj_idx = [item["vertex"] for item in sorted_registry]

    # Transpose graph
    inverted_adj = get_inversed_adj(adj)

    # Do DFS on the transpose graph but using the sorted vertex by finishing time
    visited = [0] * len(inverted_adj)
    components = []

    for i in sorted_adj_idx:
        if visited[i] == 0:
            component = dfs2(i, inverted_adj, visited, [])
            components.append(component)

    return len(components)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(number_of_strongly_connected_components(adj))
