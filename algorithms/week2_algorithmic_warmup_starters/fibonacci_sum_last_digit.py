# Uses python3
import sys

def get_pisano_period(m):
    prev, curr = 0, 1
    for i in range(m * m):
        prev, curr = curr, (curr + prev) % m
        if (prev == 0) and (curr == 1): # pissano_period
            return i + 1

def fibonacci_sum_with_pisano(n, m = 10):
    pisano_period = get_pisano_period(m)
    n = n % pisano_period

    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, (previous + current) % m
        sum = (sum + current) % m

    return sum

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum_with_pisano(n))
