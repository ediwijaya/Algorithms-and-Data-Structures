#Uses python3

import sys
import random

def is_greater_than_or_equal(digit, max_digit):
    if max_digit == float('-inf'):
        return True
    return int(str(digit) + str(max_digit)) >= int(str(max_digit) + str(digit))

def largest_number(llist):
    #write your code here
    res = ""
    max_idx = None
    while len(llist) > 0:
        max_digit = float('-inf')
        for i, val in enumerate(llist):
            if is_greater_than_or_equal(val, max_digit):
                max_idx = i
                max_digit = llist[max_idx]
        res += llist.pop(max_idx)
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))