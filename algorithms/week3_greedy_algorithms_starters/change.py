# Uses python3
import sys

def get_change(m):
    counter = 0
    change = 0
    while change < m:
        if (change + 10) <= m:
            change += 10
        elif (change + 5) <= m:
            change += 5
        elif (change + 1) <= m:
            change += 1
        counter += 1
    return counter

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))