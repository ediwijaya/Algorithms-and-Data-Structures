#Uses python3
import subprocess
import sys
import unittest

sys.setrecursionlimit(40000)

def dfs(adj, v, visited, order):
    visited[v] = True
    for w in adj[v]:
        if not visited[w]:
            dfs(adj, w, visited, order)
    order.append(v)

def get_reverse_postorder(adj):
    visited = [0] * len(adj)
    order = []
    for v in range(len(adj)):
        if not visited[v]:
            dfs(adj, v, visited, order)
    return order[::-1]

def explore(adj, v, visited, scc, scc_counter):
    visited[v] = True
    scc[v] = scc_counter
    for w in adj[v]:
        if not visited[w]:
            explore(adj, w, visited, scc, scc_counter)

def number_of_strongly_connected_components(adj, adj_rev):
    postorder_rev = get_reverse_postorder(adj_rev)
    visited = [False] * len(adj)
    scc = [0] * len(adj)
    scc_counter = 1
    for v in postorder_rev:
        if not visited[v]:
            explore(adj, v, visited, scc, scc_counter)
            scc_counter += 1
    return len(set(scc))

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
""",
                "2",
            ),
            (
                "sample_2",
                """\
3 3
1 2
2 3
1 3
""",
                "3",
            ),
            (
                "sample_3",
                """\
4 3
1 2
3 1
4 1
""",
                "4",
            ),
            (
                "sample_4",
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
                "5",
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
    edges_rev = [(b, a) for (a, b) in edges]
    adj_rev = [[] for _ in range(n)]
    for (a, b) in edges_rev:
        adj_rev[a - 1].append(b - 1)
    print(number_of_strongly_connected_components(adj, adj_rev))
