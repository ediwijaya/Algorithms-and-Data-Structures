# Uses python3
import sys
import numpy as np

def optimal_weight(W, bars):
    # write your code here
    value = np.zeros([len(bars)+1, W+1], dtype=int)
    for i in range(1, len(bars) + 1):
        for w in range(1, W+1):
            value[i, w] = value[i-1, w]
            if bars[i-1] <= w:
                temp_val = bars[i-1] + value[i-1, w-bars[i-1]]
                if value[i, w] < temp_val:
                    value[i, w] = temp_val
    return value[-1, -1]

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
