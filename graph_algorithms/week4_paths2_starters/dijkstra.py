#Uses python3
import heapq
import subprocess
import sys
import unittest

sys.setrecursionlimit(500000)


def distance(adj, cost, s, t):
    #write your code here
    """Find a shortest directed path weight using heap-based Dijkstra.

    Requires nonnegative edge weights. For n vertices and m edges,
    time is O((n + m) log(n + m)) and auxiliary space is O(n + m)
    because the heap can contain outdated entries. Total space
    including input and graph storage is O(n + m).

    Args:
        adj: Zero-based adjacency lists of a directed graph.
        cost: Parallel weights; cost[u][i] belongs to u -> adj[u][i].
        s: Source vertex index.
        t: Target vertex index.

    Returns:
        The shortest path weight, or -1 if t is unreachable.

    Example:
        >>> distance([[1], []], [[7], []], 0, 1)
        7"""
    dist = dijkstra(adj, s, cost)
    return dist[t] if dist[t] < float('inf') else -1

def dijkstra(adj, A, cost):
    """Compute shortest distances using a heap with lazy priority updates.

    All vertices initially enter the heap, with only A at distance
    zero. Improvements push new entries; entries with an outdated
    distance are skipped before scanning edges. The predecessor list
    is maintained internally but is not returned. With n vertices and
    m edges, time is O((n + m) log(n + m)) and auxiliary space is O(n + m).
    Edge weights must be nonnegative.

    Args:
        adj: Zero-based adjacency lists of a directed graph.
        A: Source vertex index.
        cost: Weights aligned by position with each adjacency list.

    Returns:
        Minimum distances from A; unreachable vertices retain infinity."""
    prev = [None] * len(adj)
    dist = [float('inf')] * len(adj)

    dist[A] = 0
    heap = []
    for v in range(len(dist)):
        heapq.heappush(heap, (dist[v], v))
    while heap:
        queued_dist, u = heapq.heappop(heap)
        if queued_dist > dist[u]:
            continue
        for i, v in enumerate(adj[u]):
            if dist[v] > dist[u] + cost[u][i]:
                dist[v] = dist[u] + cost[u][i]
                prev[v] = u
                heapq.heappush(heap, (dist[v], v))
    return dist

class TestCases(unittest.TestCase):
    """Tests for cases."""

    def test_sample_inputs(self) -> None:
        """Check complete program input and output."""
        cases = [
            (
                "sample_1",
                """\
4 4
1 2 1
4 1 2
2 3 2
1 3 5
1 3
""",
                "3",
            ),
            (
                "sample_2",
                """\
5 9
1 2 4
1 3 2
2 3 2
3 2 1
2 4 2
3 5 4
5 4 1
2 5 3
3 4 4
1 5
""",
                "6",
            ),
(
                "sample_3",
                """\
3 3
1 2 7
1 3 5
2 3 2
3 2
""",
                "-1",
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
                self.assertEqual(result.stdout.strip(), expected)


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))
