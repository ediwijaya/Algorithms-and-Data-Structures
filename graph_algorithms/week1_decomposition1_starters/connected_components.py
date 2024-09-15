#Uses python3

import sys

def explore(v):
    global visited, adj, ccnum, cc
    visited[v] = True
    cc_num[v] = cc
    for w in adj[v]:
        if not visited[w]:
            explore(w)

def depth_search_first(graph):
    global visited, cc
    for v in range(len(graph)):
        if not visited[v]:
            explore(v)
            cc += 1

def number_of_components(adj):
    depth_search_first(adj)
    return len(set(cc_num))

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    visited = [False for _ in range(len(adj))]
    cc_num = [-1 for _ in range(len(adj))]
    cc = 0
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(number_of_components(adj))

# python reachability.py <<< "4 2" <<< "1 2" <<< "3 2"