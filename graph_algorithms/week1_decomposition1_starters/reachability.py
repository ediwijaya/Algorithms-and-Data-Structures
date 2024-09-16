#Uses python3

import sys

class Graph:
    def __init__(self, num_vertex, num_edge) -> None:
        self.num_vertex = num_vertex
        self.num_edge = num_edge
        self.visited = [False] * num_vertex
        self.pre = [0] * num_vertex
        self.post = [0] * num_vertex
        self.cc_num = [-1] * num_vertex # connectivity_cluster_num
        self.cc = 0 # connectivity_cluster
        self.clock = 0
        self.adj = [[] * self.num_vertex]

    def assign_adj(self, adj) -> None:
        self.adj = adj
    
    def previsit(self, v) -> None:
        self.pre[v] = self.clock
        self.clock += 1

    def postvisit(self, v) -> None:
        self.post[v] = self.clock
        self.clock += 1

    def explore(self, v) -> None:
        self.visited[v] = True
        self.cc_num[v] = self.cc
        for w in self.adj[v]:
            if not self.visited[w]:
                self.explore(w)

    def depth_first_search(self) -> None:
        for v in range(self.num_vertex):
            if not self.visited[v]:
                self.explore(v)
                self.cc += 1

    def reach(self, adj, x, y) -> int:
        self.assign_adj(adj)
        self.depth_first_search()
        return int(self.cc_num[x] == self.cc_num[y])

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    x, y = data[2 * m:]
    adj = [[] for _ in range(n)]
    graph = Graph(num_vertex=n, num_edge=m)
    x, y = x - 1, y - 1
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(graph.reach(adj, x, y))

# python reachability.py <<< "4 4" <<< "1 2" <<< "3 2" <<< "4 3" <<< "1 4" <<< "1 4"
# python reachability.py <<< "4 2" <<< "1 2" <<< "3 2" <<< "1 4"