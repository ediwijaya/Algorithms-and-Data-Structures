# Uses python3
import sys

def get_pisano_period(m):
    prev, curr = 0, 1
    for i in range(m * m):
        prev, curr = curr, (curr + prev) % m
        if (prev == 0) and (curr == 1): # pissano_period
            return i + 1

def get_fibonacci_huge_naive_modulo(n, m):
    pisano_period = get_pisano_period(m)
    n = n % pisano_period

    if (n <= 1):
        return n
    else:
        curr = 1
        prev = 0
        for _ in range(n-1):
            curr, prev = curr + prev, curr
    return curr % m

if __name__ == '__main__':
    input = sys.stdin.read()
    n, m = map(int, input.split())
    print(get_fibonacci_huge_naive_modulo(n, m))