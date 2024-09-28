#Uses python3

import sys

def negative_cycle(adj, cost):
    """
    In Bellman-Ford Algorithms for non negative cycle graph, it is guaranteed that in V-1 iteration,
    all edges has been shortest. Thus, if in V-th iteration the program still relaxing edge,
    it is has negative cycle(s).
    """
    n_vertex = len(adj)
    dist = [sys.maxsize] * n_vertex
    dist[0] = 0
    for _ in range(n_vertex - 1): # repeat V-1 times
        for u in range(n_vertex): # use dynamic programming, Bellman-ford for non-negative cycle graph
            for i, v in enumerate(adj[u]): # to access w(u,v), we should use its relative index
                if dist[v] > dist[u] + cost[u][i]: # as the implementation is array.
                    dist[v] = dist[u] + cost[u][i]
    for u in range(n_vertex): # check negative cycle
        for i, v in enumerate(adj[u]):
            if dist[v] > dist[u] + cost[u][i]:
                return 1
    return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    print(negative_cycle(adj, cost))

# python negative_cycle.py <<< "4 4" <<< "1 2 -5" <<< "4 1 2" <<< "2 3 2" <<< "3 1 1"
# python negative_cycle.py <<< "4 3" <<< "1 2 -5" <<< "2 3 2" <<< "3 1 1"