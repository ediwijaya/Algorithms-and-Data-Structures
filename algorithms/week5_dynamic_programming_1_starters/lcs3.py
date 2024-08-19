#Uses python3
import sys
import numpy as np

def lcs3(a, b, c):
    #write your code here
    max_i = len(a) + 1
    max_j = len(b) + 1
    max_k = len(c) + 1
    dist = np.zeros([max_i, max_j, max_k], dtype=int)
    
    for i in range(1, max_i):
        for j in range(1, max_j):
            for k in range(1, max_k):
                match = dist[i - 1, j - 1, k - 1] + 1
                not_match_1 = dist[i - 1, j, k]
                not_match_2 = dist[i, j - 1, k]
                not_match_3 = dist[i, j, k - 1]
                if a[i - 1] == b[j - 1] == c[k - 1]:
                    dist[i, j, k] = match
                else:
                    dist[i, j, k] = max(not_match_1, not_match_2, not_match_3)
    total_edist = dist[-1, -1, -1]
    return total_edist

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    print(lcs3(a, b, c))
