# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.key = [0 for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.right = [0 for i in range(self.n)]
        for i in range(self.n):
            [a, b, c] = map(int, sys.stdin.readline().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c

    def inOrder(self):
        self.result = []
        def in_order_traversal(node=0):
            if node == -1:
                return
            in_order_traversal(self.left[node])
            self.result.append(self.key[node])
            in_order_traversal(self.right[node])
        in_order_traversal()
        return self.result

    def preOrder(self):
        self.result = []
        def pre_order_traversal(node=0):
            if node == -1:
                return
            self.result.append(self.key[node])
            pre_order_traversal(self.left[node])
            pre_order_traversal(self.right[node])
        pre_order_traversal()
        return self.result

    def postOrder(self):
        self.result = []
        def post_order_traversal(node=0):
            if node == -1:
                return
            post_order_traversal(self.left[node])
            post_order_traversal(self.right[node])
            self.result.append(self.key[node])
        post_order_traversal()
        return self.result

def main():
	tree = TreeOrders()
	tree.read()
	print(" ".join(str(x) for x in tree.inOrder()))
	print(" ".join(str(x) for x in tree.preOrder()))
	print(" ".join(str(x) for x in tree.postOrder()))

threading.Thread(target=main).start()

class Tree:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.key = [0 for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.right = [0 for i in range(self.n)]
        for i in range(self.n):
            [a, b, c] = map(int, sys.stdin.readline().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c

    def inOrder(self):
        self.result = []
        def in_order_traversal(node=0):
            if node == -1:
                return
            in_order_traversal(self.left[node])
            self.result.append(self.key[node])
            in_order_traversal(self.right[node])
        in_order_traversal()
        return self.result