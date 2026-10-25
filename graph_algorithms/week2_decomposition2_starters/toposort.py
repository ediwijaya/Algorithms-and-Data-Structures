#Uses python3
import subprocess
import sys
import unittest

sys.setrecursionlimit(500000)

def dfs(adj, v, visited, order):
    visited[v] = True
    for w in adj[v]:
        if not visited[w]:
            dfs(adj, w, visited, order)
    order.append(v)

def toposort(adj):
    visited = [0] * len(adj)
    order = []
    for v in range(len(adj)):
        if not visited[v]:
            dfs(adj, v, visited, order)
    return order[::-1]

class TestCases(unittest.TestCase):
    """Tests for cases."""

    def test_sample_inputs(self) -> None:
        """Check complete program input and output."""
        cases = [
            (
                "sample_1",
                """\
4 3
1 2
4 1
3 1
""",
                "4 3 1 2",
            ),
            (
                "sample_1",
                """\
5 7
2 1
3 2
3 1
4 3
4 1
5 2
5 3
""",
                "5 4 3 2 1",
            ),
            (
                "sample_3",
                """\
4 1
3 1
""",
                "2 3 1 4",
            ),
        ]

        for name, input_text, _ in cases:
            with self.subTest(case=name):
                result = subprocess.run(
                    [sys.executable, __file__],
                    input=input_text,
                    text=True,
                    capture_output=True,
                    check=True,
                )
                actual = list(map(int, result.stdout.split()))
                data = list(map(int, input_text.split()))
                n, m = data[:2]

                # Every vertex must appear exactly once.
                self.assertCountEqual(actual, range(1, n + 1))

                # Map each vertex to its position in the output.
                position = {vertex: index for index, vertex in enumerate(actual)}

                # Every edge u -> v requires u to appear before v.
                for i in range(m):
                    u, v = data[2 + 2 * i : 4 + 2 * i]
                    self.assertLess(
                        position[u],
                        position[v],
                        msg=f"Edge {u} -> {v}: {u} must appear before {v}",
                    )

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    order = toposort(adj)
    for x in order:
        print(x + 1, end=' ')

