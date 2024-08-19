# Uses python3
import sys

def get_fibonacci_last_digit_naive(n):
    if (n <= 1):
        return n
    else:
        curr = 1
        prev = 0
        for _ in range(n-1):
            curr, prev = (curr + prev)%10, curr%10
    return curr

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit_naive(n))
