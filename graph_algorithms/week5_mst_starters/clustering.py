#Uses python3
import math
import subprocess
import sys
import unittest


class Point:
    """Store a point's Cartesian coordinates for distance calculations."""
    def __init__(self, x: int, y: int) -> None:
        """Store the supplied x- and y-coordinates without modification.

        Args:
            x: X-coordinate of the point.
            y: Y-coordinate of the point.
        """
        self.x = x
        self.y = y

def get_dist(point_1, point_2):
    """Calculate the Euclidean distance between two points.

    Time and auxiliary space are O(1) for assignment-sized coordinates.

    Args:
        point_1: First Point instance.
        point_2: Second Point instance.

    Returns:
        The nonnegative straight-line distance between the points.
    """
    return math.sqrt((point_1.x - point_2.x)**2 + (point_1.y - point_2.y)**2)

class UnionFind:
    """Data Structures and Algorithms for Disjoint Set Union"""
    def __init__(self, n: int) -> None:
        """Initiate the Disjoin Set Union.

        Args:
            n: Total number of node/vertex in graph.
        """
        self.parents = list(range(n))
        self.rank = [0] * n
        self.components = n

    def find(self, x: int) -> int:
        """Perform finding parent of vertex using log* complexity.
        
        Args:
            x: Vertex we want to get the parent for.
        
        Returns:
            Parent of vertex x.
        """
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, a: int, b: int) -> bool:
        root_a, root_b = self.find(a), self.find(b)

        if root_a == root_b:
            return False
        if self.rank[root_a] < self.rank[root_b]: # make sure it is always left union where left always gte right
            root_a, root_b = root_b, root_a # swap value
        self.parents[root_b] = root_a
        if self.rank[root_a] == self.rank[root_b]: # This state is guaranteed by swap that rank root_a >= root_b
            self.rank[root_a] += 1 # Adjust the rank as ran root_a is now higher than root_b
        self.components -= 1
        return True

    def connected(self, a: int, b: int) -> bool:
        return self.find(a) == self.find(b)

def clustering(x, y, k) -> float:
    """Cluster min distance between k clusters k of (x, y) points coordinate using Kruskal's Algorithm.

    Algorithms:
        1. Calculate distance edges between all points O(n * (n-1)).
            Create `cluster_edge`, a integer, to record which edge belong to in a cluster.
            Its default is None, which mean it does not belongs to any.
        2. Initiate n = len(point) cluster (each point is its own cluster).
        3. For each points, add shorted edges not in its own cluster. Cluster them using UnionFind.
        4. Repeat step 3 until n cluster is k.
        5. Create dummy program by copying last n-k state.
        6. Continue another for final k+1 next edge to join and return it is value.
        The problem becomes (n - k + 1)th successful merged edge.

    Args:

    Returns:
        The minimum distance of between any points in different cluster(max of the minimum).
    """
    point = [Point(x, y) for x, y in zip(x, y)]
    adj = [[] for _ in range(len(point))]
    cost = []
    for i in range(len(adj)):
        for j in range(len(adj)):
            if i != j:
                adj[i].append(j)
                cost.append((get_dist(point[i], point[j]), i, j)) # format list of (cost, i, j)
    

    # Perform Kruskal's Algorithms
    sorted_cost_indices = [i for i, _ in sorted(enumerate(cost), key=lambda x: x[1][0])]
    n = len(point)
    uf = UnionFind(n) # each i is its own vertex index
    counter = 0
    last_idx = 0
    boundary = n - k + 1
    for idx in sorted_cost_indices:
        if counter < boundary:
            # Get index i and j of the idx edge
            curr_edge = cost[idx]
            i, j = curr_edge[1], curr_edge[2]
            if uf.union(i, j):
                counter += 1
        else:
            last_idx = idx
            break
    result = cost[last_idx][0]
    return result

class TestCases(unittest.TestCase):
    """Tests for cases."""

    def test_sample_inputs(self) -> None:
        """Check complete program input and output."""
        cases = [
            (
                "sample_1",
                """\
12
7 6
4 3
5 1
1 7
2 7
5 7
3 3
7 8
2 8
4 4
6 7
2 6
3
""",
                "2.828427124746",
            ),
            (
                "sample_2",
                """\
8
3 1
1 2
4 6
9 8
9 9
8 9
3 11
4 12
4
""",
                "5.000000000",
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
    data = data[1:]
    x = data[0:2 * n:2]
    y = data[1:2 * n:2]
    data = data[2 * n:]
    k = data[0]
    print(f"{clustering(x, y, k):.9f}")
