#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

def is_binary_search_tree(tree):
    # Implement correct algorithm here
    in_order_list = []
    def in_order_traversal(node=0):
        if node == -1:
            return
        value, left, right = tree[node]
        in_order_traversal(left)
        in_order_list.append(value)
        in_order_traversal(right)
    result = True
    if len(tree) <= 1:
        return result
    in_order_traversal()
    for i in range(len(in_order_list) - 1):
        if in_order_list[i] > in_order_list[i+1]:
            result = False
    return result

def main():
    nodes = int(sys.stdin.readline().strip())
    tree = []
    for i in range(nodes):
        tree.append(list(map(int, sys.stdin.readline().strip().split())))
    if is_binary_search_tree(tree):
        print("CORRECT")
    else:
        print("INCORRECT")

threading.Thread(target=main).start()

# python is_bst_hard.py <<< "4" <<< "4 1 -1" <<< "2 2 3" <<< "1 -1 -1" <<< "5 -1 -1"
# python is_bst_hard.py <<< "7" <<< "4 1 2" <<< "2 3 4" <<< "6 5 6" <<< "1 -1 -1" <<< "3 -1 -1" <<< "5 -1 -1" <<< "7 -1 -1"
# python is_bst_hard.py <<< "5" <<< "1 -1 1" <<< "2 -1 2" <<< "3 -1 3" <<< "4 -1 4" <<< "5 -1 -1"