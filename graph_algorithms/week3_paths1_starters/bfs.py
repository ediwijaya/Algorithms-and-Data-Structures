#Uses python3

import sys
from collections import deque

def breadth_first_search(adj, origin):
    dist = [float('inf')] * len(adj)
    dist[origin] = 0
    q = deque()
    q.append(origin)
    while len(q) > 0:
        u = q.popleft()
        for v in adj[u]:
            if dist[v] == float('inf'):
                q.append(v)
                dist[v] = dist[u] + 1
    return dist

def distance(adj, s, t):
    #write your code here
    dist = breadth_first_search(adj, s)
    return -1 if dist[t] == float('inf') else dist[t]

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(distance(adj, s, t))

# python bfs.py <<< "4 4" <<< "1 2" <<< "4 1" <<< "2 3" <<< "3 1" <<< "2 4"
# python bfs.py <<< "5 4" <<< "5 2" <<< "1 3" <<< "3 4" <<< "1 4" <<< "3 5"