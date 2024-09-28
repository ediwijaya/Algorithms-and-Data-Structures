#Uses python3

import sys
import queue

def distance(adj, cost, s, t):
    #write your code here
    num_v = len(adj)
    dist = [float('inf')] * num_v
    prev = [None] * num_v
    dist[s] = 0 # Initiate source to 0
    heap = list(dist) # Implement heap as list
    for _ in range(len(heap)-1):
        u = heap.index(min(heap))
        for i, v in enumerate(adj[u]): # to access w(u,v), we should use its relative index
            if dist[v] > dist[u] + cost[u][i]: # as the implementation is array.
                dist[v] = dist[u] + cost[u][i]
                prev[v] = u
                heap[v] = dist[v]
        heap[u] = float('inf') # equivalent to remove this queue

    return -1 if dist[t] == float('inf') else dist[t]


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
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))

# python dijkstra.py <<< "4 4" <<< "1 2 1" <<< "4 1 2" <<< "2 3 2" <<< "1 3 5" <<< "1 3"
### output: 3
# python dijkstra.py <<< "5 9" <<< "1 2 4" <<< "1 3 2" <<< "2 3 2" <<< "3 2 1" <<< "2 4 2" <<< "3 5 4" <<< "5 4 1" <<< "2 5 3" <<< "3 4 4" <<< "1 5"
### output: 6
# python dijkstra.py <<< "3 3" <<< "1 2 7" <<< "1 3 5" <<< "2 3 2" <<< "3 2"
### output: -1