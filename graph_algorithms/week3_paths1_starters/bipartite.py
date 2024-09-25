#Uses python3

import sys
from collections import deque

def bipartite(adj):
    len_adj = len(adj)
    visited = [False] * len_adj
    color = [-1] * len_adj

    for v in range(len_adj):
        q = deque()
        q.append(v)
        while q:
            u = q.popleft()
            if not visited[u]: # not visited yet
                visited[u] = True
                for w in adj[u]:
                    if not visited[w]: # already visited, check for consistency
                        q.append(w) # not yet visited
                        color[w] = 1 - color[u]
                    else:
                        if color[w] == color[u]:
                            return 0
    return 1

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
    print(bipartite(adj))

# python bipartite.py <<< "4 4" <<< "1 2" <<< "4 1" <<< "2 3" <<< "3 1"
# python bipartite.py <<< "5 4" <<< "5 2" <<< "4 2" <<< "3 4" <<< "1 4"