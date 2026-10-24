#Uses python3
import subprocess
import sys
import unittest

sys.setrecursionlimit(5000)

def number_of_components(adj):
    visited = [False] * len(adj)
    cc_group = [0] * len(adj)
    counter = 1
    #write your code here
    for v in range(len(adj)):
        if not visited[v]:
            explore(v, adj, visited, counter, cc_group)
            counter += 1
    return len(set(cc_group))

def explore(v, adj, visited, counter, cc_group):
    visited[v] = True
    cc_group[v] = counter
    for w in adj[v]:
        if not visited[w]:
            explore(w, adj, visited, counter, cc_group)

class TestReach(unittest.TestCase):
    """Tests for graph reachability."""

    def test_sample_inputs(self) -> None:
        """Check complete program input and output."""
        cases = [
            (
                "sample_1",
                """\
4 4
1 2
3 2
4 3
1 4
""",
                "1",
            ),
            (
                "sample_1",
                """\
4 2
1 2
3 2
""",
                "2",
            ),
            (
                "sample_3",
                """\
3 0
""",
                "3",
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
    print(number_of_components(adj))
