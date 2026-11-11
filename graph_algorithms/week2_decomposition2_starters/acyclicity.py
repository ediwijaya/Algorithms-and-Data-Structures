#Uses python3
import subprocess
import sys
import unittest

sys.setrecursionlimit(5000)

class Clock:
    """Track a shared counter for DFS entry and exit timestamps."""
    def __init__(self):
        """Initialize the traversal counter to zero."""
        self.counter = 0

    def increment(self):
        """Advance the shared timestamp by one in O(1) time."""
        self.counter += 1


def acyclic(adj):
    """Detect a directed cycle using unfinished DFS vertices.

    Despite the function name, the result is 1 when a cycle exists.
    An edge to a visited vertex with no postorder timestamp indicates
    a back edge to the active recursion path. For n vertices and m
    adjacency entries, time is O(n + m), auxiliary space is O(n), and
    total space with the graph is O(n + m).

    Args:
        adj: Zero-based adjacency lists of a directed graph.

    Returns:
        1 if the graph contains a directed cycle, otherwise 0.

    Example:
        >>> acyclic([[1], [0]])
        1"""
    visited = [False] * len(adj)
    is_cyclic = [False]
    clock = Clock()
    preorder = [None] * len(adj)
    postorder = [None] * len(adj)
    for v in range(len(adj)):
        if not visited[v]:
            explore(adj, v, visited, is_cyclic, clock, preorder, postorder)
    return int(is_cyclic[0])

def explore(adj, v, visited, is_cyclic, clock, preorder, postorder):
    """Explore a DFS tree and flag back edges to unfinished vertices.

    Entry and exit timestamps and discovery flags are mutated in place.
    A discovered vertex lacking an exit timestamp is still on the active
    DFS path. Worst-case time is O(n + m) and stack space is O(n).

    Args:
        adj: Zero-based adjacency lists of a directed graph.
        v: Vertex to explore.
        visited: Shared discovery flags.
        is_cyclic: One-element Boolean list storing cycle detection.
        clock: Shared Clock instance used for traversal timestamps.
        preorder: Shared entry timestamps, initially None.
        postorder: Shared exit timestamps, initially None."""
    clock.increment()
    preorder[v] = clock.counter
    visited[v] = True
    for w in adj[v]:
        if not visited[w]:
            explore(adj, w, visited, is_cyclic, clock, preorder, postorder)
        else:
            if postorder[w] is None:
                is_cyclic[0] = True
                break
    clock.increment()
    postorder[v] = clock.counter


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
