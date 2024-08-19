# Uses python3
import sys

def get_change(m):
    #write your code here
    # case when m <= 4
    change_list = [1, 2, 1, 1]
    if m <= 4:
        return change_list[m-1]
    # case when m > 4
    for i in range(5, m + 1):
        option_add1 = change_list[i-2] + 1
        option_add3 = change_list[i-4] + 1
        option_add4 = change_list[i-5] + 1
        min_change = min(option_add1, option_add3, option_add4)
        change_list.append(min_change)
    return change_list[-1]

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))