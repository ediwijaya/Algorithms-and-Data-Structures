#Uses python3
import queue
import subprocess
import sys
import unittest

sys.setrecursionlimit(500000)

def bipartite(adj):
    #write your code here
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
    """Compute shortest-path distances from a source vertex using BFS.

    Args:
        adj: Adjacency list representing the graph.
        a: Zero-based index of the source vertex (root).

    Returns:
        A list of distances from ``a`` to each vertex. Unreachable vertices
        have an infinite distance.
    """
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
