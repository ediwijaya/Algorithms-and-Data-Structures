# Uses python3
import sys
import numpy as np

def partition3(item_weight):
    n = len(item_weight)
    total_weight = sum(item_weight)
    if n < 3:
        return 0
    elif total_weight % 3 != 0:
        return 0
    else:
        count = 0
        target_weight = total_weight // 3
        arr_val = np.zeros([n + 1, target_weight + 1], dtype=int)
        for i in range(1, n + 1):
            for w in range(1, target_weight + 1):
                arr_val[i, w] = arr_val[i - 1, w]
                if item_weight[i - 1] <= w:
                    temp = arr_val[i - 1 , w - item_weight[i - 1]] + item_weight[i - 1]
                    if temp > arr_val[i, w]:
                        arr_val[i, w] = temp
                if arr_val[i, w] == target_weight:
                    count += 1
        if count >= 3:
            return 1
        else:
            return 0
        
# A = 2, 4, 4,6, 8
# n = 5
# W = 8
#    1 2 3 4 5 6 7 8
#  0 0 0 0 0 0 0 0 0
#2 0 0 2 2 2 2 2 2 2
#4 0 0 0 0 4 4 6 6 6
#4 0 0 0 0 4 4 6 6 8
#6 0 0 0 0 0 0 6 6 8
#8 0 0 0 0 0 0 0 0 8


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    print(partition3(A))