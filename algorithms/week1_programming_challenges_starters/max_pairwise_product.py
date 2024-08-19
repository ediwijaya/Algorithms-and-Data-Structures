# using python3
import random
# n = int(input())
# a = [int(x) for x in input().split()]
# assert len(a) == n

def max_pairwise_product_sorted(a):
    a.sort(reverse=True)
    return a[0]*a[1]

def max_pairwise_product_naive(a):
    result = 0
    n = len(a)
    for i in range(0, n):
        for j in range(i+1, n):
            if a[i]*a[j] > result:
                result = a[i]*a[j]
    return result

def max_pairwise_product_fast(a):
    if a[0] > a[1]:
        first = a[0]
        second = a[1]
    else:
        first = a[1]
        second = a[0]
    if len(a) > 2:
        for x in a[2:]:
            if x > second:
                if x > first:
                    second = first
                    first = x
                else:
                    second = x

    return first * second

def stress_test(N, M):
    while True:
        n = random.randint(2, N)
        A = list(random.randint(0, M) for r in range(n))
        print(A)
        result_naive = max_pairwise_product_naive(A)
        result_fast = max_pairwise_product_fast(A)
        if result_naive == result_fast:
            print('OK')
        else:
            print(f"Wrong answer: {result_naive}, {result_fast}")
            break


stress_test(10, 1000)