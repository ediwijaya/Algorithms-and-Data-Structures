# Uses python3
import numpy as np

def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def MinAndMax(i, j, min_arr, max_arr, ops):
    min_val = float('inf')
    max_val = float('-inf')
    for k in range(i, j):
        a = evalt(max_arr[i, k], max_arr[k+1, j], ops[k])
        b = evalt(max_arr[i, k], min_arr[k+1, j], ops[k])
        c = evalt(min_arr[i, k], max_arr[k+1, j], ops[k])
        d = evalt(max_arr[i, k], min_arr[k+1, j], ops[k])
        min_val = min(min_val, a, b, c, d)
        max_val = max(max_val, a, b, c, d)
    return min_val, max_val

def get_maximum_value(dataset):
    nums = [int(x) for x in dataset[::2]]
    ops = [x for x in dataset[1::2]]
    #write your code here
    n = len(nums)
    min_arr = np.full([n, n], np.nan)
    max_arr = np.full([n, n], np.nan)
    for i in range(n):
        min_arr[i, i] = nums[i]
        max_arr[i, i] = nums[i]

    for s in range(1, n):
        for i in range(0, n-s):
            j = i + s
            min_arr[i, j], max_arr[i, j] = MinAndMax(i, j, min_arr, max_arr, ops)
    return int(max_arr[0, n-1])

if __name__ == "__main__":
    print(get_maximum_value(input()))
