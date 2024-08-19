# Uses python3
import numpy as np

def edit_distance(s, t):
    #write your code here
    max_i = len(s) + 1
    max_j = len(t) + 1
    dist = np.zeros([max_i, max_j],dtype=int)
    for i in range(max_i):
        dist[i, 0] = i
    for j in range(max_j):
        dist[0, j] = j
    
    for i in range(1, max_i):
        for j in range(1, max_j):
            insertion = dist[i, j - 1] + 1
            deletion = dist[i - 1, j] + 1
            match = dist[i - 1, j - 1]
            replace = dist[i - 1, j - 1] + 1
            if s[i - 1] == t[j - 1]:
                dist[i, j] = min(insertion, deletion, match)
            else:
                dist[i, j] = min(insertion, deletion, replace)
    return dist[-1, -1]

if __name__ == "__main__":
    print(edit_distance(input(), input()))
