#Uses python3
import copy
import subprocess
import sys
import unittest

sys.setrecursionlimit(10000)


def shortest_paths(adj, cost, s, distance, reachable, shortest):
    # Perform V-1 iteration of Bellman-Ford
    distance[s] = 0
    reachable[s] = 1
    for _ in range(len(adj) - 1):
        for v in range(len(adj)):
            for i, u in enumerate(adj[v]):
                if distance[u] > distance[v] + cost[v][i]:
                    distance[u] = distance[v] + cost[v][i]
                    if reachable[u] == 0:
                        reachable[u] = 1

    temp_distance = copy.deepcopy(distance)
    # Perform 1 more iteration or 5th loop for detection of negative cycle
    for _ in range(len(adj)):
        for v in range(len(adj)):
            for i, u in enumerate(adj[v]):
                if distance[u] > distance[v] + cost[v][i]:
                    distance[u] = distance[v] + cost[v][i]

    for i in range(len(distance)):
        if distance[i] != temp_distance[i]:
            shortest[i] = 0

class TestCases(unittest.TestCase):
    """Tests for cases."""

    def test_sample_inputs(self) -> None:
        """Check complete program input and output."""
        cases = [
            (
                "sample_1",
                """\
6 7
1 2 10
2 3 5
1 3 100
3 5 7
5 4 10
4 3 -18
6 1 -1
1
""",
                """\
0
10
-
-
-
*
""",
            ),
            (
                "sample_2",
                """\
5 4
1 2 1
4 1 2
2 3 2
3 1 -5
4
""",
                """\
-
-
-
0
*
""",
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
                self.assertEqual(result.stdout.strip(), expected.strip())


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
    s = data[0]
    s -= 1
    distance = [float('inf')] * n
    reachable = [0] * n
    shortest = [1] * n
    shortest_paths(adj, cost, s, distance, reachable, shortest)
    for x in range(n):
        if reachable[x] == 0:
            print('*')
        elif shortest[x] == 0:
            print('-')
        else:
            print(distance[x])

