#Uses python3
import sys
import math

class Node:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

def find(v):
    if parent[v] != v:
        parent[v] = find(parent[v])
    return parent[v]

def union(i, j):
    global parent
    parent[find(j)] = find(i)
    find(j) # Update parent j using rank heuristic
    
def convert_to_vertices_list(x_list, y_list):
    result = []
    for i in range(len(x_list)):
        result.append(Node(x_list[i], y_list[i]))
    return result

def calc_distance(node_1, node_2):
    return math.sqrt((node_1.x - node_2.x)**2 + (node_1.y - node_2.y)**2)

def clustering(x, y, k):
    global parent
    n_point = len(x)
    vertices = convert_to_vertices_list(x, y)
    edge_list = []
    n_cluster = len(x)
    for i in range(n_point): # calculate all possible combination of all point
        for j in range(i+1, n_point):
            dist = calc_distance(vertices[i], vertices[j])
            edge_list.append((dist, i, j))
    # At maximum, we do it for V*(V-1)/2. Example: V=8, we should have at max 28 elm in edge list
    # Based on this approach, it is guarenteed that i > j
    # Thus, using union rank heuristic and lowest index, Union(i, j) can just assign parent[j] as find(i)
    edge_sorted = sorted(edge_list)
    for distance, i, j in edge_sorted:
        if find(i) != find(j):
            if n_cluster == k:
                break
            union(i, j)
            n_cluster -= 1
    return distance

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    data = data[1:]
    x = data[0:2 * n:2]
    y = data[1:2 * n:2]
    parent = [x for x in range(n)]
    data = data[2 * n:]
    k = data[0]
    print("{0:.9f}".format(clustering(x, y, k)))

# python clustering.py <<< "12" <<< "7 6" <<< "4 3" <<< "5 1" <<< "1 7" <<< "2 7" <<< "5 7" <<< "3 3" <<< "7 8" <<< "2 8" <<< "4 4" <<< "6 7" <<< "2 6" <<< "3"
# python clustering.py <<< "8" <<< "3 1" <<< "1 2" <<< "4 6" <<< "9 8" <<< "9 9" <<< "8 9" <<< "3 11" <<< "4 12" <<< "4"