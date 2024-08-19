#Uses python3
import sys
import numpy as np

def lcs2(a, b):
    #write your code here
    max_i = len(a) + 1
    max_j = len(b) + 1
    dist = np.zeros([max_i, max_j],dtype=int)
    
    for i in range(1, max_i):
        for j in range(1, max_j):
            match = dist[i - 1, j - 1] + 1
            not_match_2 = dist[i - 1, j]
            not_match_3 = dist[i, j - 1]
            if a[i - 1] == b[j - 1]:
                dist[i, j] = match
            else:
                dist[i, j] = max(not_match_2, not_match_3)
    total_edist = dist[-1, -1]
    return total_edist

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))
