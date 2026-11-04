#Uses python3
import subprocess
import sys
import unittest

sys.setrecursionlimit(10000)

def negative_cycle(adj, cost):
    dist = [sys.maxsize] * len(adj)
    for _ in range(len(adj) - 1):
        for u in range(len(adj)):
            for i, v in enumerate(adj[u]):
                dist[v] = min(dist[v], dist[u] + cost[u][i])
    copy_dist = dist.copy()
    # perform one last time to check changes in V-th run
    for u in range(len(adj)):
        for i, v in enumerate(adj[u]):
            copy_dist[v] = min(copy_dist[v], copy_dist[u] + cost[u][i])
    return 1 - int(copy_dist == dist)

class TestCases(unittest.TestCase):
    """Tests for cases."""

    def test_sample_inputs(self) -> None:
        """Check complete program input and output."""
        cases = [
            (
                "sample_1",
                """\
4 4
1 2 -5
4 1 2
2 3 2
3 1 1
""",
                "1",
            ),
            (
                "sample_2",
                """\
3 3
1 2 7
1 3 5
2 3 2
""",
                "0",
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
    print(negative_cycle(adj, cost))
