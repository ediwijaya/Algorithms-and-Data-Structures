#Uses python3

import sys

sys.setrecursionlimit(200000)

class GraphDirected:
    def __init__(self, num_vertex, num_edge) -> None:
        self.num_vertex = num_vertex
        self.num_edge = num_edge
        self.visited = [False] * self.num_vertex
        self.pre = [0] * self.num_vertex
        self.post = [0] * self.num_vertex
        self.cc_num = [-1] * self.num_vertex # connectivity_cluster_num
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

    def get_idx_postorder_reversed(self) -> list:
        reverse_ordered_post = list(zip(self.post, [i for i in range(0, len(self.post))]))
        reverse_ordered_post = sorted(reverse_ordered_post, reverse=True)
        reverse_ordered_post = [idx for rank, idx in reverse_ordered_post]
        return reverse_ordered_post

    def number_of_strongly_connected_components(self, reversed_adj, adj) -> int:
        self.assign_adj(reversed_adj)
        self.depth_first_search()
        reverse_ordered_post = self.get_idx_postorder_reversed()
        # reset neccessary attributes
        self.assign_adj(adj)
        self.visited = [False] * self.num_vertex
        self.cc_num = [-1] * self.num_vertex
        self.cc = 0
        for v in reverse_ordered_post:
            if not self.visited[v]:
                self.explore(v)
            self.cc += 1
        result = len(set(self.cc_num))
        return result
    
def reverse_edge(edges) -> list:
    reversed_edge = []
    for u, v in edges:
        reversed_edge.append((v, u))
    return reversed_edge

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    adj_r = [[] for _ in range(n)]
    edges_r = reverse_edge(edges)
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    for (a, b) in edges_r:
        adj_r[a - 1].append(b - 1)
    graph = GraphDirected(n, m)
    print(graph.number_of_strongly_connected_components(adj_r, adj))

# python strongly_connected.py <<< "4 4" <<< "1 2" <<< "4 1" <<< "2 3" <<< "3 1"
### adj = [[1], [2], [0], [0]]
### adj_r = [[3, 2], [0], [1], []]
# python strongly_connected.py <<< "5 7"<<< "2 1" <<< "3 2" <<< "3 1" <<< "4 3" <<< "4 1" <<< "5 2" <<< "5 3"
### adj = [[], [0], [1, 0], [2, 0], [1, 2]]
### adj_r = [[1, 2, 3], [2, 4], [3, 4], [], []]