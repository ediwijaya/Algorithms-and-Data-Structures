#Uses python3

import sys

class GraphDirected:
    def __init__(self, num_vertex, num_edge) -> None:
        self.num_vertex = num_vertex
        self.num_edge = num_edge
        self.visited = [False] * num_vertex
        self.pre = [0] * num_vertex
        self.post = [0] * num_vertex
        self.cc_num = [-1] * num_vertex # connectivity_cluster_num
        self.cc = 0 # connectivity_cluster
        self.clock = 1
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
        self.previsit(v)
        self.cc_num[v] = self.cc
        for w in self.adj[v]:
            if not self.visited[w]:
                self.explore(w)
        self.postvisit(v)

    def depth_first_search(self) -> None:
        for v in range(self.num_vertex):
            if not self.visited[v]:
                self.explore(v)
                self.cc += 1

    def reach(self, adj, x, y) -> int:
        self.assign_adj(adj)
        self.depth_first_search()
        return int(self.cc_num[x] == self.cc_num[y])
    
    def acyclic(self, adj) -> int:
        self.cyclic = False
        self.assign_adj(adj)
        for v in range(self.num_vertex):
            self.origin_vertex = v
            self.visited = [False] * self.num_vertex # to assign new cycle after each connectivity
            if not self.visited[v]:
                self.explore(v)
            if self.cyclic:
                break
        return int(self.cyclic)
    
    def topological_sort(self, adj) -> int:
        self.assign_adj(adj)
        self.depth_first_search()
        reverse_ordered_post = list(zip(self.post, [i for i in range(0, len(self.post))]))
        reverse_ordered_post = sorted(reverse_ordered_post, reverse=True)
        reverse_ordered_post = [idx for rank, idx in reverse_ordered_post]
        return reverse_ordered_post


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    graph = GraphDirected(num_vertex=n, num_edge=m)
    order = graph.topological_sort(adj)
    for x in order:
        print(x + 1, end=' ')

# python toposort.py <<< "4 3" <<< "1 2" <<< "4 1" <<< "3 1"
# python toposort.py <<< "4 1" <<< "3 1"
# python toposort.py <<< "5 7"<<< "2 1" <<< "3 2" <<< "3 1" <<< "4 3" <<< "4 1" <<< "5 2" <<< "5 3"