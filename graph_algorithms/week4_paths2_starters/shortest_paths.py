#Uses python3

import sys
import queue

def bfs(adj, q):
    while not q.empty(): # we BFS all the Q (which contains negative cycle)
        u = q.get()
        for v in adj[u]:
            if shortest[v]:
                shortest[v] = 0 # Note each of vertex of Q as not shortest
                q.put(v)

def shortest_paths(adj, cost, s, distance, reachable, shortest):
    """
    In Bellman-Ford Algorithms for non negative cycle graph, it is guaranteed that in V-1 iteration,
    all edges has been shortest. Thus, if in V-th iteration the program still relaxing edge,
    it is has negative cycle(s).
    """
    n_vertex = len(adj)
    distance[s] = 0 # A vertex distance from itself is always 0
    reachable[s] = 1 # A vertex always reachable from itself
    for _ in range(n_vertex - 1): # repeat V-1 times
        for u in range(n_vertex): # use dynamic programming, Bellman-ford for non-negative cycle graph
            for i, v in enumerate(adj[u]): # to access w(u,v), we should use its relative index
                if distance[v] > distance[u] + cost[u][i]: # as the implementation is array.
                    distance[v] = distance[u] + cost[u][i]
                    reachable[v] = 1
    q = queue.Queue()
    for u in range(n_vertex): # check negative cycle, the V-the iteration
        for i, v in enumerate(adj[u]): # to access w(u,v), we should use its relative index
            if distance[v] > distance[u] + cost[u][i]: # as the implementation is array.
                shortest[v] = 0
                q.put(v) # put all node of A into q
    bfs(adj, q)

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
    s = data[0]
    s -= 1
    distance = [float('inf')] * n # I was getting error for case 6/36.
    # I suspect it is because we need to make very big number. Thus, make it float('inf')
    reachable = [0] * n
    shortest = [1] * n
    shortest_paths(adj, cost, s, distance, reachable, shortest)
    for x in range(n):
        if reachable[x] == 0:
            print('*')
        elif shortest[x] == 0:
            print('-')
        else:
            print(distance[x])

# python shortest_paths.py <<< "6 7" <<< "1 2 10" <<< "2 3 5" <<< "1 3 100" <<< "3 5 7" <<< "5 4 10" <<< "4 3 -18" <<< "6 1 -1" <<< "1"
# python shortest_paths.py <<< "5 4" <<< "1 2 1" <<< "4 1 2" <<< "2 3 2" <<< "3 1 -5" <<< "4"