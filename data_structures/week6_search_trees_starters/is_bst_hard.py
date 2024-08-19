#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left if left != -1 else None
        self.right = right if right != -1 else None
    
class Tree:
    def __init__(self):
        self.nodes = []
        self.root = None
        self.value_inorder = []
        self.result_inorder = []

    def read(self):
        self.n = int(sys.stdin.readline())
        
        for _ in range(self.n):
            value, left, right = map(int, sys.stdin.readline().strip().split())
            self.nodes.append(Node(value, left, right))

        if self.n > 0:
            self.root = self.nodes[0]

    def in_order_traversal(self, node):
        if node is None:
            return
        if node.left:
            self.in_order_traversal(self.nodes[node.left])
        self.value_inorder.append(node.value)

        if node.left and node.right:
            if self.nodes[node.left].value < node.value <= self.nodes[node.right].value:
                self.result_inorder.append(True)
            else:
                self.result_inorder.append(False)
        elif node.left:
            if self.nodes[node.left].value < node.value:
                self.result_inorder.append(True)
            else:
                self.result_inorder.append(False)
        elif node.right:
            if node.value <= self.nodes[node.right].value:
                self.result_inorder.append(True)
            else:
                self.result_inorder.append(False)
        else:
            self.result_inorder.append(True)

        if node.right:
            self.in_order_traversal(self.nodes[node.right])

    def is_bst(self):
        if self.n <= 1:
            return True
        
        self.in_order_traversal(self.root)
        result = self.value_inorder
        for i in range(self.n - 1):
            if result[i] > result[i + 1]:
                return False
        return True
    
    def is_bst_hard(self):
        if self.n <= 1:
            return True
        self.in_order_traversal(self.root)
        result = self.value_inorder
        for i in range(self.n - 1):
            if result[i] > result[i + 1]:
                return False
        print(self.result_inorder)
        return True #all(self.result_inorder)

def main():
    tree = Tree()
    tree.read()
    tree.in_order_traversal(tree.root)
    print(tree.value_inorder)
    if tree.is_bst_hard():
        print("CORRECT")
    else:
        print("INCORRECT")

threading.Thread(target=main).start()

# python is_bst_hard.py <<< "4" <<< "4 1 -1" <<< "2 2 3" <<< "1 -1 -1" <<< "5 -1 -1"
# python is_bst_hard.py <<< "7" <<< "4 1 2" <<< "2 3 4" <<< "6 5 6" <<< "1 -1 -1" <<< "3 -1 -1" <<< "5 -1 -1" <<< "7 -1 -1"
# python is_bst_hard.py <<< "5" <<< "1 -1 1" <<< "2 -1 2" <<< "3 -1 3" <<< "4 -1 4" <<< "5 -1 -1"