#Uses python3
import heapq
import math
import subprocess
import sys
import unittest


class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

def minimum_distance(x, y): # MST Problem. We can use either Kruskal or Prims algo. We use Prims variant here with assumption N*(N-1)/2 edges.
    point = [Point(x, y) for x, y in zip(x, y)]

    # start the adjacency list and weight calculation:
    adj = [[] for _ in range(len(point))]
    cost = [[] for _ in range(len(point))]
    for i in range(len(point)):
        for j in range(len(point)):
            if i != j:
                adj[i].append(j)
                cost[i].append(get_dist(point[i], point[j]))

    # start the Prim's algorithms
    result = 0.
    dist = [float('inf')] * len(point)
    parent = [None] * len(point)
    in_tree = [False] * len(point)

    start_vertex = 0
    dist[start_vertex] = 0
    heap = []
    for i in range(len(point)):
        heapq.heappush(heap, (dist[i], i))

    while heap:
        curr_cost, v = heapq.heappop(heap)
        if in_tree[v]:
            continue
        else:
            in_tree[v] = True
            result += curr_cost
            for i, u in enumerate(adj[v]):
                if (not in_tree[u]) and (dist[u] > cost[v][i]):
                    dist[u] = cost[v][i]
                    parent[u] = v
                    heapq.heappush(heap, (cost[v][i], u))
    return result

def get_dist(point_1, point_2):
    return math.sqrt((point_1.x - point_2.x)**2 + (point_1.y - point_2.y)**2)

class TestCases(unittest.TestCase):
    """Tests for cases."""

    def test_sample_inputs(self) -> None:
        """Check complete program input and output."""
        cases = [
            (
                "sample_1",
                """\
4
0 0
0 1
1 0
1 1
""",
                "3.00000000",
            ),
            (
                "sample_2",
                """\
5
0 0
0 2
1 1
3 0
3 2
""",
                "7.064495102",
            ),
        ]

        for name, input_text, expected in cases:
            with self.subTest(case=name):
                result = subprocess.run(
                    [sys.executable, __file__],
                    input=input_text,
                    text=True,
                    capture_output=True,
                    check=True,
                )
                self.assertAlmostEqual(
    float(result.stdout.strip()),
    float(expected),
    delta=1e-6,
)


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print(f"{minimum_distance(x, y):.9f}")
