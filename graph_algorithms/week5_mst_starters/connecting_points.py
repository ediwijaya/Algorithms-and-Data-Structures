#Uses python3
import heapq
import math
import subprocess
import sys
import unittest


class Point:
    """Store a point's Cartesian coordinates for distance calculations."""
    def __init__(self, x, y) -> None:
        """Store the supplied x- and y-coordinates without modification.

        Args:
            x: X-coordinate of the point.
            y: Y-coordinate of the point.
        """
        self.x = x
        self.y = y

def minimum_distance(x: list[int], y: list[int]) -> float:
    """Compute the Euclidean MST weight using linear-scan Prim.

    Edge distances are calculated on demand. Each of n rounds scans the
    points to update connection costs and select the next outside vertex.
    Time is O(n^2); auxiliary and total space are O(n), including the
    temporary selection list and point objects.

    Args:
        x: X-coordinates of the nonempty set of points.
        y: Matching y-coordinates, with the same length as x.

    Returns:
        The minimum total length needed to connect all points.

    Example:
        >>> minimum_distance([0, 3], [0, 4])
        5.0
    """
    point = [Point(x, y) for x, y in zip(x, y)]

    # start the Prim's algorithms
    result = 0.
    dist = [float('inf')] * len(point)
    in_tree = [False] * len(point)

    curr_vertex = 0
    dist[curr_vertex] = 0
    curr_min_dist = dist[curr_vertex]

    for _ in range(len(point)):
        in_tree[curr_vertex] = True
        result += curr_min_dist
        for j in range(len(point)):
            if curr_vertex != j:
                temp_dist = get_dist(point[curr_vertex], point[j])
                if (not in_tree[j]) and (dist[j] > temp_dist):
                    dist[j] = temp_dist

        if sum(in_tree) < len(in_tree):
            dist_not_in_tree = [d if not in_tree[i] else float('inf') for i, d in enumerate(dist)]
            curr_min_dist = min(dist_not_in_tree)
            curr_vertex = dist_not_in_tree.index(curr_min_dist)
        else:
            break
    
    return result

def minimum_distance_heap(x: list[int], y: list[int]) -> float:
    """Compute the Euclidean MST weight using the previous heap-based Prim.

    This preserves the earlier implementation for comparison with
    minimum_distance: construct the complete graph, then grow the tree
    using a min-heap of candidate connection costs. Improved costs create
    new entries; entries for vertices already accepted are skipped.

    For n points, graph construction takes O(n^2) time and space. There
    can be O(n^2) heap entries in total, each costing O(log n) to push or
    pop. Overall time is O(n^2 log n), and auxiliary and total space are
    O(n^2). The parent list records chosen connections but is not returned.

    Args:
        x: X-coordinates of the nonempty set of points.
        y: Matching y-coordinates, with the same length as x.

    Returns:
        The minimum total length needed to connect all points.

    Example:
        >>> minimum_distance_heap([0, 3], [0, 4])
        5.0
    """
    point = [Point(x, y) for x, y in zip(x, y)]
    adj = [[] for _ in range(len(point))]
    cost = [[] for _ in range(len(point))]
    for i in range(len(point)):
        for j in range(len(point)):
            if i != j:
                adj[i].append(j)
                cost[i].append(get_dist(point[i], point[j]))

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
    """Calculate the Euclidean distance between two points.

    Time and auxiliary space are O(1) for assignment-sized coordinates.

    Args:
        point_1: First Point instance.
        point_2: Second Point instance.

    Returns:
        The nonnegative straight-line distance between the points."""
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
