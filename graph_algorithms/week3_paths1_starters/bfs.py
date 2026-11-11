#Uses python3
import queue
import subprocess
import sys
import unittest

sys.setrecursionlimit(500000)

def distance(adj, s, t):
    """Find the minimum number of edges between two vertices using BFS.

    For n vertices and m adjacency entries, time is O(n + m) and
    auxiliary space is O(n), including distances and the BFS queue.
    Total space including the supplied graph is O(n + m).

    Args:
        adj: Zero-based adjacency lists of an unweighted graph.
        s: Source vertex index.
        t: Target vertex index.

    Returns:
        The shortest edge count, or -1 if t is unreachable from s.

    Example:
        >>> distance([[1], [0, 2], [1]], 0, 2)
        2"""
    #write your code here
    dist = bfs(adj, s)
    return dist[t] if dist[t] != float('inf') else -1

def bfs(adj, a):
    """Compute unweighted distances from a source in breadth-first order.

    A finite distance also records that a vertex has been discovered,
    so each reachable vertex enters the queue once. The predecessor
    list is maintained internally but is not returned. For n vertices
    and m adjacency entries, time is O(n + m) and auxiliary space is O(n).

    Args:
        adj: Zero-based adjacency lists of an unweighted graph.
        a: Source vertex index.

    Returns:
        Distances measured in edges; unreachable vertices retain infinity."""
    dist = [float('inf')] * len(adj)
    prev = [None] * len(adj)
    dist[a] = 0
    q = queue.Queue()
    q.put(a)
    while not q.empty():
        u = q.get()
        for v in adj[u]:
            if dist[v] == float('inf'):
                q.put(v)
                dist[v] = dist[u] + 1
                prev[v] = u
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
1 2
4 1
2 3
3 1
2 4
""",
                "2",
            ),
            (
                "sample_2",
                """\
5 4
5 2
1 3
3 4
1 4
3 5
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
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(distance(adj, s, t))
