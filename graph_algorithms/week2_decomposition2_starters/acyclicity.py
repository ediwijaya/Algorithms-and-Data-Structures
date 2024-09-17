#Uses python3

import sys

class GraphDirected:
    def __init__(self, num_vertex, num_edge) -> None:
        self.num_vertex = num_vertex
        self.num_edge = num_edge
        self.visited = [False] * num_vertex
        # self.pre = [0] * num_vertex
        # self.post = [0] * num_vertex
        # self.cc_num = [-1] * num_vertex # connectivity_cluster_num
        # self.cc = 0 # connectivity_cluster
        self.clock = 1
        self.adj = [[] * self.num_vertex]

    def assign_adj(self, adj) -> None:
        self.adj = adj
    
    # def previsit(self, v) -> None:
    #     self.pre[v] = self.clock
    #     self.clock += 1

    # def postvisit(self, v) -> None:
    #     self.post[v] = self.clock
    #     self.clock += 1

    def explore(self, v) -> None:
        self.visited[v] = True
        for w in self.adj[v]:
            if w == self.origin_vertex:
                self.cyclic = True
                break
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
    
    def acyclic(self, adj) -> int:
        self.cyclic = False
        self.assign_adj(adj)
        # print(self.adj)
        for v in range(self.num_vertex):
            self.origin_vertex = v
            self.visited = [False] * self.num_vertex # to assign new cycle after each connectivity
            if not self.visited[v]:
                self.explore(v)
            if self.cyclic:
                break
        return int(self.cyclic)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    graph = GraphDirected(num_vertex=n, num_edge=m)
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(graph.acyclic(adj))

# python acyclicity.py <<< "4 4" <<< "1 2" <<< "4 1" <<< "2 3" <<< "3 1"
### [[1], [2], [0], [0]]
# python acyclicity.py <<< "5 7" <<< "1 2" <<< "2 3" <<< "1 3" <<< "3 4" <<< "1 4" <<< "2 5" <<< "3 5"
### [[1, 2, 3], [2, 4], [3, 4], [], []]



    # def topological_sort(self, adj) -> int:
    #     # If graph G contains cycle, it cannot be linearly ordered. Thus, if it is linearly ordered, it does not contains cycle (acyclic).
    #     # A graph G is DAG if it has no cycles (acyclic).
    #     # Any DAG can be linearly ordered.

    #     # If is is a DAG, then it is acyclic.
    #     # We can use is_dag to determine if it is cyclic or acyclic.

    #     self.assign_adj(adj)
    #     self.depth_first_search()
    #     reverse_ordered_post = list(zip(self.post, [i for i in range(1, len(self.post) + 1)]))
    #     print(reverse_ordered_post)
    #     reverse_ordered_post = sorted(reverse_ordered_post, reverse=True)
    #     reverse_ordered_post = [idx for rank, idx in reverse_ordered_post]
    #     return reverse_ordered_post