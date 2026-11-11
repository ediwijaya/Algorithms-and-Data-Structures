#Uses python3
import subprocess
import sys
import unittest

sys.setrecursionlimit(5000)

def number_of_components(adj):
    """Count connected components by labeling each DFS tree.

    A new component label is assigned whenever an unvisited vertex starts
    an exploration. The number of distinct labels gives the answer.
    For n vertices and m adjacency entries, time is O(n + m), auxiliary
    space is O(n) including labels, the set, and recursion, and total
    space with graph storage is O(n + m).

    Args:
        adj: Zero-based adjacency lists of an undirected graph.

    Returns:
        The number of connected components.

    Example:
        >>> number_of_components([[1], [0], []])
        2"""
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
    """Assign one component label to every vertex reachable from v.

    Worst-case time is O(n + m) and recursion space is O(n).

    Args:
        v: Starting vertex index.
        adj: Zero-based adjacency lists of the undirected graph.
        visited: Shared discovery flags, updated in place.
        counter: Label for this connected component.
        cc_group: Shared component labels, updated in place."""
    visited[v] = True
    cc_group[v] = counter
    for w in adj[v]:
        if not visited[w]:
            explore(w, adj, visited, counter, cc_group)

class TestCases(unittest.TestCase):
    """Tests cases."""

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
