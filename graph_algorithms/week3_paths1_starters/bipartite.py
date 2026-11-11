#Uses python3
import queue
import subprocess
import sys
import unittest

sys.setrecursionlimit(500000)

def bipartite(adj):
    #write your code here
    """Check two-colorability using BFS levels followed by DFS validation.

    BFS assigns finite levels separately in every component. Level
    parity defines a proposed color, and DFS checks that every edge
    joins different colors. For n vertices and m adjacency entries,
    time is O(n + m), auxiliary space is O(n) including queue and
    recursion, and total space with graph storage is O(n + m).

    Args:
        adj: Zero-based adjacency lists of an undirected graph.

    Returns:
        1 if the graph is bipartite, otherwise 0.

    Example:
        >>> bipartite([[1], [0], []])
        1"""
    is_bipartite = [True]
    dist = bfs(adj)
    color_map = [x % 2 for x in dist] # make sure that odd is 1 and even is 0
    visited = [False] * len(adj)
    # perform dfs
    for v in range(len(adj)):
        if not visited[v] and is_bipartite[0]:
            explore(adj, v, visited, color_map, is_bipartite)
        else:
            continue
    return int(is_bipartite[0])

def bfs(adj):
    """Assign BFS distances from one chosen root per component.

    Each unvisited component root starts at distance zero, preserving
    levels assigned in previous components. Every vertex is eventually
    reached, including isolated vertices. The predecessor list is
    internal and is not returned. Time is O(n + m) and auxiliary space
    is O(n) for n vertices and m adjacency entries.

    Args:
        adj: Zero-based adjacency lists of an undirected graph.

    Returns:
        Finite edge-count distances from each vertex's component root."""
    dist = [float('inf')] * len(adj)
    visited = [False] * len(adj)
    prev = [None] * len(adj)
    q = queue.Queue()
    for a in range(len(visited)):
        if not visited[a]:
            dist[a] = 0
            q.put(a)
            visited[a] = True
            while not q.empty():
                u = q.get()
                for v in adj[u]:
                    if dist[v] == float('inf'):
                        q.put(v)
                        visited[v] = True
                        dist[v] = dist[u] + 1
                        prev[v] = u
        else:
            continue
    return dist

def explore(adj, v, visited, color_map, is_bipartite):
    """Check that edges in a DFS exploration connect opposite colors.

    Mutates visited and sets is_bipartite[0] to False on a conflict.
    The flag is shared across recursive calls. Worst-case time is
    O(n + m) and recursion space is O(n).

    Args:
        adj: Zero-based adjacency lists of the graph.
        v: Vertex to explore.
        visited: Shared discovery flags.
        color_map: Proposed colors, 0 or 1, derived from BFS levels.
        is_bipartite: One-element Boolean list recording validity."""
    visited[v] = True
    curr_color = color_map[v]
    expected_next_color = (curr_color + 1) % 2
    for w in adj[v]:
        if expected_next_color != color_map[w]:
            is_bipartite[0] = False
            break
        else:
            if not visited[w]:
                explore(adj, w, visited, color_map, is_bipartite)


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
                "0",
            ),
            (
                "sample_2",
                """\
5 4
5 2
4 2
3 4
1 4
""",
                "1",
            ),
            (
                "sample_3",
                """\
4 2
1 3
2 4
""",
                "1",
            ),
            (
                "sample_4",
                """\
5 4
1 2
3 4
4 5
5 3
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
        adj[b - 1].append(a - 1)
    print(bipartite(adj))
