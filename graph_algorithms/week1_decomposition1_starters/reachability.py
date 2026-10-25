#Uses python3
import subprocess
import sys
import unittest

sys.setrecursionlimit(5000)

def reach(adj, x, y):
    #write your code here
    visited = [False] * len(adj)
    explore(adj, x, visited, target=y)
    return int(visited[y])

def explore(adj, v, visited, target):
    visited[v] = True
    for w in adj[v]:
        if w == target:
            visited[w] = True
            break
        if not visited[w]:
            explore(adj, w, visited, target)
            if visited[target] == True:
                break

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
3 2
4 3
1 4
1 4
""",
                "1",
            ),
            (
                "sample_1",
                """\
4 2
1 2
3 4
1 4
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
    x, y = data[2 * m:]
    adj = [[] for _ in range(n)]
    x, y = x - 1, y - 1
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(reach(adj, x, y))
