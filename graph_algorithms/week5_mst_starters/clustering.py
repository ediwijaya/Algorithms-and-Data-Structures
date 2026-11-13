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
    """Maintain disjoint sets with union by rank and path compression.

    Tracks connected components across vertices labeled from 0 to n - 1.
    Operations achieve near-constant amortized time proportional to the
    inverse Ackermann function alpha(n).
    """
    def __init__(self, n: int) -> None:
        """Initialize disjoint sets for n individual vertices.

        Args:
            n: Total number of vertices in the graph.
        """
        self.parents = list(range(n))
        self.rank = [0] * n
        self.components = n

    def find(self, x: int) -> int:
        """Find the representative root of the set containing vertex x.

        Applies path compression to flatten the tree during traversal,
        achieving near-constant amortized lookup time.

        Args:
            x: Vertex index whose root representative is requested.

        Returns:
            The representative root index of vertex x.
        """
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, a: int, b: int) -> bool:
        """Merge the sets containing vertices a and b using union by rank.

        If a and b belong to distinct sets, the root with lower rank is
        attached beneath the root with higher rank. If ranks are equal,
        one becomes the parent and its rank is incremented.

        Args:
            a: First vertex index.
            b: Second vertex index.

        Returns:
            True if the sets were merged, or False if a and b already
            belonged to the same set.
        """
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
        """Check whether vertices a and b belong to the same component.

        Args:
            a: First vertex index.
            b: Second vertex index.

        Returns:
            True if a and b have the same representative root, else False.
        """
        return self.find(a) == self.find(b)

def clustering(x: list[int], y: list[int], k: int) -> float:
    """Compute the maximum spacing of a k-clustering using Kruskal's algorithm.

    Pairwise Euclidean distances are computed across all point pairs to form
    a complete undirected edge list of size n(n - 1)/2. Edges are sorted in
    ascending order by distance. A Union-Find data structure iteratively merges
    components until reaching the threshold boundary (n - k + 1) successful
    merges, extracting the minimum distance between points in different clusters.

    For n points and k clusters, generating edges takes O(n^2) time and space.
    Sorting the n(n - 1)/2 edges takes O(n^2 log n) time. Disjoint-set operations
    take O(n^2 * alpha(n)) time. Overall time is O(n^2 log n), and auxiliary and
    total space are O(n^2).

    Args:
        x: X-coordinates of the points.
        y: Y-coordinates of the points, matching x in length.
        k: Number of non-empty clusters to form (2 <= k <= len(x)).

    Returns:
        The maximum value d such that the distance between any two points
        from different clusters is at least d.

    Example:
        >>> clustering([3, 1, 4, 9, 9, 8, 3, 4], [1, 2, 6, 8, 9, 9, 11, 12], 4)
        5.0
    """
    point = [Point(x, y) for x, y in zip(x, y)]
    cost = []
    for i in range(len(point)):
        for j in range(i+1, len(point)):
            cost.append((get_dist(point[i], point[j]), i, j)) # list of (cost, i, j) tuple
    

    # Perform Kruskal's Algorithms
    cost.sort(key=lambda edge: edge[0])
    n = len(point)
    uf = UnionFind(n)
    counter = 0
    result = 0.
    boundary = n - k + 1
    for dist, i, j in cost:
        if counter < boundary:
            if uf.union(i, j):
                counter += 1
            if counter == boundary:
                result = dist
                break
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
