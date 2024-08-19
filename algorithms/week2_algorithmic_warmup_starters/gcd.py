# Uses python3
import sys

def gcd_euclidean(a, b):
    if b > a:
        a, b = b, a # reverse to make sure a >= b

    if a % b == 0:
        return b
    else:
        a_prime = a % b
        return gcd_euclidean(b, a_prime)

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd_euclidean(a, b))
