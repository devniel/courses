class Program:
    def dfs(self, curr, des, adj, vis):
        # If current node is the destination, return True
        if curr == des:
            return True
        vis[curr] = 1
        for x in adj[curr]:
            if not vis[x]:
                if self.dfs(x, des, adj, vis):
                    return True
        return False

    def isPath(self, src, des, adj):
        vis = [0] * (len(adj) + 1)
        return self.dfs(src, des, adj, vis)

    def findSCC(self, n, a):
        # Stores all the strongly connected components
        strongly_connected_components = []

        # Stores whether a vertex is a part of any Strongly Connected Component
        is_scc = [0] * (n + 1)

        # Create adjacency list
        adj = [[] for _ in range(n + 1)]

        for i in range(len(a)):
            adj[a[i][0]].append(a[i][1])

        print(f"Adjacency list: {adj}")

        # Traversing all the vertices N
        for i in range(1, n+1):
            if not is_scc[i]:
                # If a vertex i is not a part of any SCC, insert it into a new SCC list
                scc = [i]
                for j in range(i+1, n+1):
                    # If there is a path from vertex i to vertex j and vice versa,
                    # put vertex j into the current SCC list
                    if not is_scc[j] and self.isPath(i, j, adj) and self.isPath(j, i, adj):
                        is_scc[j] = 1
                        scc.append(j)
                # Insert the SCC containing vertex i into the final list
                strongly_connected_components.append(scc)

        return strongly_connected_components

if __name__ == "__main__":
    obj = Program()
    V = 5
    edges = [
        [1, 3],
        [1, 4],
        [2, 1],
        [3, 2],
        [4, 5]
    ]
    ans = obj.findSCC(V, edges)
    print("Strongly Connected Components are:")
    for x in ans:
        for y in x:
            print(y, end=" ")
        print()
