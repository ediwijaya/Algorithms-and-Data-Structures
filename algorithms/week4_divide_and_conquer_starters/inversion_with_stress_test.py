# Uses python3
import sys, random

def merge_sorted_list_efficient(left, right):
    result = []
    num_inversion = 0
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
            num_inversion += len(left)
    result.extend(left)
    result.extend(right)
    return result, num_inversion

def merge_sort_with_inversion_efficient(a):
    num_inversion = 0
    left = 0
    right = len(a)
    if right <= 1:
        return a, num_inversion
    mid = left + (right - left) // 2
    left_recursion, left_inv = merge_sort_with_inversion_efficient(a[left: mid])
    num_inversion += left_inv
    right_recursion, right_inv = merge_sort_with_inversion_efficient(a[mid: right])
    num_inversion += right_inv
    sorted_list, tmp_inversion = merge_sorted_list_efficient(left_recursion, right_recursion)
    num_inversion += tmp_inversion
    return sorted_list, num_inversion

def merge_sorted_list(left, right):
    result = []
    i, j, num_inversion = 0, 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            num_inversion += len(left) - i
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result, num_inversion

def merge_sort_with_inversion(a):
    num_inversion = 0
    left = 0
    right = len(a)
    if right <= 1:
        return a, num_inversion
    mid = left + (right - left) // 2
    left_recursion, left_inv = merge_sort_with_inversion(a[left: mid])
    num_inversion += left_inv
    right_recursion, right_inv = merge_sort_with_inversion(a[mid: right])
    num_inversion += right_inv
    sorted_list, tmp_inversion = merge_sorted_list(left_recursion, right_recursion)
    num_inversion += tmp_inversion
    return sorted_list, num_inversion

def stress_test(N, M):
    while True:
        n = random.randint(2, N)
        A = list(random.randint(0, M) for r in range(n))
        print(A)
        result_naive = merge_sort_with_inversion(A)[1]
        result_fast = merge_sort_with_inversion_efficient(A)[1]
        if result_naive == result_fast:
            print('OK')
        else:
            print(f"Wrong answer: {result_naive}, {result_fast}")
            break

stress_test(10, 10)