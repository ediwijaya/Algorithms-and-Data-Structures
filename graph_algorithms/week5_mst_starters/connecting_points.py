#Uses python3
import sys
import math
import heapq

class Node:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

def calc_distance(node_1, node_2):
    return math.sqrt((node_1.x - node_2.x)**2 + (node_1.y - node_2.y)**2)

def convert_to_vertices_list(x_list, y_list):
    result = []
    for i in range(len(x_list)):
        result.append(Node(x_list[i], y_list[i]))
    return result

def minimum_distance(x, y):
    result = 0
    n_point = len(x)
    vertices = convert_to_vertices_list(x, y)

    cost = [float('inf')] * n_point
    parent = [None] * n_point
    solution = []
    cost[0] = 0 # Distance to itself is always 0
    q = [(cost, i) for i, cost in enumerate(cost)]
    heapq.heapify(q)
    while q:
        _, v = heapq.heappop(q)
        solution.append(v)
        for z in range(n_point):
            if z not in solution and cost[z] > calc_distance(vertices[z], vertices[v]):
                cost[z] = calc_distance(vertices[z], vertices[v])
                parent[z] = v
                heapq.heappush(q, (cost[z], z))
    return sum(cost)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))

# python connecting_points.py <<< "4" <<< "0 0" <<< "0 1" <<< "1 0" <<< "1 1"
# python connecting_points.py <<< "5" <<< "0 0" <<< "0 2" <<< "1 1" <<< "3 0" <<< "3 2"