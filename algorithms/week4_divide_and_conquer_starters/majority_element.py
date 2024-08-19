# Uses python3
import sys

def get_majority_element(elm_list):
    counter = {}
    for elm in elm_list:
        if elm in counter.keys():
            counter[elm] += 1
        else:
            counter[elm] = 1
    max_occurence = max(counter.values())
    return 1 if max_occurence > len(elm_list) / 2 else 0

def get_majority_element_divnconq(elm_list, start, end):
    # base case
    if start == end:
        return elm_list[start]
    
    # sub problem
    mid = (start + end) // 2

    left = get_majority_element_divnconq(elm_list, start, mid)
    right = get_majority_element_divnconq(elm_list, mid + 1, end)
    
    focus_list = elm_list[start:end]

    if left == right:
        return left
    elif focus_list.count(left) > focus_list.count(right):
        return left
    else:
        return right

def wrapper(elm_list, start, end):
    majority_elm = get_majority_element_divnconq(elm_list, start, end)
    counter_elm = elm_list.count(majority_elm)
    if counter_elm > len(elm_list) / 2:
        return 1
    else:
        return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    print(wrapper(a, 0, n - 1))
