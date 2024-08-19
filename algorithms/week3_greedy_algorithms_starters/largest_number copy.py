#Uses python3

import sys
import random

def is_greater_than_or_equal_fast(digit, max_digit):
    if max_digit == float('-inf'):
        return True
    return int(str(digit) + str(max_digit)) >= int(str(max_digit) + str(digit))

def is_greater_than_or_equal(digit, max_digit):
    if max_digit == float('-inf'):
        return True
    # return int(str(digit) + str(max_digit)) >= int(str(max_digit) + str(digit))
    
    len_digit = len(digit)
    len_max_digit = len(max_digit)
    flag = False
    i = 0
    while (len_digit > 0) and (len_max_digit > 0):
        s1, s2 = digit[i], max_digit[i]
        if s1 < s2:
            break
        if s1 > s2:
            flag = True
            break
        len_digit -= 1
        len_max_digit -= 1
        if len_digit == 0:
            flag = True
            break
        if len_max_digit == 0:
            flag = False
            break
        i += 1
    return flag

def stress_test(N):
    while True:
        A = str(random.randint(1, N))
        B = str(random.randint(1, N))
        # A = list(random.randint(0, M) for _ in range(n))
        # print(A)
        result_naive = is_greater_than_or_equal(A, B)
        result_fast = is_greater_than_or_equal_fast(A, B)
        if result_naive == result_fast:
            print('OK')
        else:
            print(f"Wrong answer{A, B}: {result_naive}, {result_fast}")
            break

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

# if __name__ == '__main__':
#     input = sys.stdin.read()
#     data = input.split()
#     a = data[1:]
#     # print(largest_number(a))
stress_test(1000)