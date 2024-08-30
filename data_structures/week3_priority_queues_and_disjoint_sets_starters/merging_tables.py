# python3

import sys

n, m = map(int, sys.stdin.readline().split())
lines = list(map(int, sys.stdin.readline().split()))
rank = [1] * n
parent = list(range(0, n))
ans = max(lines)

def getParent(table): # this equivalent to find()
    # find parent and compress path
    if table != parent[table]:
        parent[table] = getParent(parent[table])
    return parent[table]

def merge(destination, source):
    global ans, lines
    realDestination, realSource = getParent(destination), getParent(source)

    if realDestination == realSource:
        return False

    # merge two components
    # use union by rank heuristic 
    # update ans with the new maximum table size
    if rank[realDestination] > rank[realSource]:
        lines[realDestination] += lines[realSource]
        lines[realSource] = 0
        parent[realSource] = realDestination
        if lines[realDestination] > ans:
            ans = lines[realDestination]
    else:
        lines[realSource] += lines[realDestination]
        lines[realDestination] = 0
        parent[realDestination] = realSource
        if rank[realSource] == rank[realDestination]:
            rank[realSource] += 1
        if lines[realSource] > ans:
            ans = lines[realSource]
    
    return True

for i in range(m):
    destination, source = map(int, sys.stdin.readline().split())
    merge(destination - 1, source - 1)
    print(ans)

# python merging_tables.py <<< "5 5" <<< "1 1 1 1 1" <<< "3 5" <<< "2 4" <<< "1 4" <<< "5 4" <<< "5 3"