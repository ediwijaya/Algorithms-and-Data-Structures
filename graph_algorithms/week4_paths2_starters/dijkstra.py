#Uses python3
import heapq
import subprocess
import sys
import unittest

sys.setrecursionlimit(500000)


def distance(adj, cost, s, t):
    #write your code here
    dist = dijkstra(adj, s, cost)
    return dist[t] if dist[t] < float('inf') else -1

def dijkstra(adj, A, cost):
    prev = [None] * len(adj)
    dist = [float('inf')] * len(adj)

    dist[A] = 0
    heap = []
    for v in range(len(dist)):
        heapq.heappush(heap, (dist[v], v))
    while heap:
        _, u = heapq.heappop(heap)
        for i, v in enumerate(adj[u]):
            if dist[v] > dist[u] + cost[u][i]:
                dist[v] = dist[u] + cost[u][i]
                prev[v] = u
                heapq.heappush(heap, (dist[v], v))
            else:
                continue
    return dist

def relax(adj, u, v, cost, prev):
    if adj[v] > adj[u] + cost[u][v]:
        adj[v] = adj[u] + cost[u][v]
        prev[v] = u


class TestCases(unittest.TestCase):
    """Tests for cases."""

    def test_sample_inputs(self) -> None:
        """Check complete program input and output."""
        cases = [
            (
                "sample_1",
                """\
4 4
1 2 1
4 1 2
2 3 2
1 3 5
1 3
""",
                "3",
            ),
            (
                "sample_2",
                """\
5 9
1 2 4
1 3 2
2 3 2
3 2 1
2 4 2
3 5 4
5 4 1
2 5 3
3 4 4
1 5
""",
                "6",
            ),
(
                "sample_3",
                """\
3 3
1 2 7
1 3 5
2 3 2
3 2
""",
                "-1",
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
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))
