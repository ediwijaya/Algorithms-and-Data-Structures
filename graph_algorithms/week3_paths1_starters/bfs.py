#Uses python3
import queue
import subprocess
import sys
import unittest

sys.setrecursionlimit(500000)

def distance(adj, s, t):
    """Compute the shortest distance from `s` to `t`
    
    Args:
        adj: Adjacency list representing the graph
        s: Zero-based index of the source of the vertex (root).
        t: Zero-based target distance form the source `s`.
    """
    #write your code here
    dist = bfs(adj, s)
    return dist[t] if dist[t] != float('inf') else -1

def bfs(adj, a):
    """Compute shortest-path distances from a source vertex using BFS.

    Args:
        adj: Adjacency list representing the graph.
        a: Zero-based index of the source vertex (root).

    Returns:
        A list of distances from ``a`` to each vertex. Unreachable vertices
        have an infinite distance.
    """
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
