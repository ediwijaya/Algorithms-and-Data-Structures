# Uses python3
import sys

def optimal_summands(n):
    i = 1
    summands = []
    while sum(summands)+i <= n:
        summands.append(i)
        i += 1
    total_sum = sum(summands)
    if total_sum == n:
        return summands
    diff = n - total_sum
    for i in range(diff):
        summands[-i-1] = summands[-i-1] + 1
    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
