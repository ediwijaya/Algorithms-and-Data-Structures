# Uses python3
def calc_fib(n):
    if (n <= 1):
        return n
    else:
        curr = 1
        prev = 0
        for _ in range(n-1):
            curr, prev = curr + prev, curr
    return curr

n = int(input())
print(calc_fib(n))