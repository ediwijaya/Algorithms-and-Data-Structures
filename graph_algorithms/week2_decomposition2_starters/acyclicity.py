#Uses python3
import subprocess
import sys
import unittest

sys.setrecursionlimit(5000)


def acyclic(adj):
    visited = [False] * len(adj)
    is_cyclic = [False]
    clock = [0]
    preorder = [None] * len(adj)
    postorder = [None] * len(adj)
    for v in range(len(adj)):
        if not visited[v]:
            explore(adj, v, visited, is_cyclic, clock, preorder, postorder)
    return int(is_cyclic[0])

def explore(adj, v, visited, is_cyclic, clock, preorder, postorder):
    clock[0] += 1
    preorder[v] = clock[0]
    visited[v] = True
    for w in adj[v]:
        if not visited[w]:
            explore(adj, w, visited, is_cyclic, clock, preorder, postorder)
        else:
            if postorder[w] is None:
                is_cyclic[0] = True
    clock[0] += 1
    postorder[v] = clock[0]


# Testing Line

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
                "1",
            ),
            (
                "sample_1",
                """\
5 7
1 2
2 3
1 3
3 4
1 4
2 5
3 5
""",
                "0",
            ),
            (
                "sample_3",
                """\
3 3
1 2
2 3
1 3
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
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))
