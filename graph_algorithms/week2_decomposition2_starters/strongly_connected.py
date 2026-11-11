#Uses python3
import subprocess
import sys
import unittest

sys.setrecursionlimit(40000)

def dfs(adj, v, visited, order):
    """Collect DFS postorder by appending each vertex after its descendants.

    Mutates visited and order. Worst-case time is O(n + m) and recursion
    space is O(n).

    Args:
        adj: Zero-based adjacency lists of a directed graph.
        v: Vertex to explore.
        visited: Shared discovery flags.
        order: Shared list collecting finishing order."""
    visited[v] = True
    for w in adj[v]:
        if not visited[w]:
            dfs(adj, w, visited, order)
    order.append(v)

def get_reverse_postorder(adj):
    """Return reversed DFS finishing order across all components.

    For n vertices and m adjacency entries, time is O(n + m) and
    auxiliary space is O(n), including recursion and the reversed copy.

    Args:
        adj: Zero-based adjacency lists of a directed graph.

    Returns:
        All vertex indices in reverse postorder."""
    visited = [0] * len(adj)
    order = []
    for v in range(len(adj)):
        if not visited[v]:
            dfs(adj, v, visited, order)
    return order[::-1]

def explore(adj, v, visited, scc, scc_counter):
    """Label the unvisited vertices reachable from v in the current pass.

    Mutates visited and scc. Worst-case time is O(n + m) and recursion
    space is O(n).

    Args:
        adj: Zero-based adjacency lists of the original directed graph.
        v: Starting vertex index.
        visited: Shared discovery flags.
        scc: Shared component labels.
        scc_counter: Label assigned to this exploration."""
    visited[v] = True
    scc[v] = scc_counter
    for w in adj[v]:
        if not visited[w]:
            explore(adj, w, visited, scc, scc_counter)

def number_of_strongly_connected_components(adj, adj_rev):
    """Count strongly connected components using two DFS passes.

    First obtain reverse postorder on the reversed graph, then explore
    the original graph in that order, labeling each DFS tree. This is
    Kosaraju's method. For n vertices and m directed edges, time is
    O(n + m) and auxiliary space is O(n), including recursion, ordering,
    labels, and their set. Total space including both graphs is O(n + m).

    Args:
        adj: Zero-based adjacency lists of the original directed graph.
        adj_rev: Adjacency lists with every original edge reversed.

    Returns:
        The number of strongly connected components.

    Example:
        >>> number_of_strongly_connected_components([[1], [0]], [[1], [0]])
        1"""
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
