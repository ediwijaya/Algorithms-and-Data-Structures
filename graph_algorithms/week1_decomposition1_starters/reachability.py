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

def reach(adj, x, y):
    #write your code here
    global cc_num
    depth_search_first(adj)
    return int(cc_num[x] == cc_num[y])

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    x, y = data[2 * m:]
    adj = [[] for _ in range(n)]
    visited = [False for _ in range(len(adj))]
    cc_num = [-1 for _ in range(len(adj))]
    cc = 0
    x, y = x - 1, y - 1
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(reach(adj, x, y))

# python reachability.py <<< "4 4" <<< "1 2" <<< "3 2" <<< "4 3" <<< "1 4" <<< "1 4"
# python reachability.py <<< "4 2" <<< "1 2" <<< "3 2" <<< "1 4"