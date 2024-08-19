# python3

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

from queue import Queue

class TreeNode:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, child_idx):
        self.children.append(child_idx)

class TreeHeight:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.parent = list(map(int, sys.stdin.readline().split()))
        self.nodes = [TreeNode(i) for i in range(self.n)]

        # add child to node
        for child_idx in range(self.n):
            parent_idx = self.parent[child_idx]
            if parent_idx == -1:
                self.root = child_idx
            else:
                self.nodes[parent_idx].add_child(self.nodes[child_idx])

    def compute_height(self):
        queue = Queue()
        queue_len = 0
        queue.put(self.nodes[self.root])
        queue_len += 1
        height = 0

        while queue_len > 0:
            height += 1
            for _ in range(queue_len):
                node = queue.get()
                queue_len -= 1
                for child in node.children:
                    queue_len += 1
                    queue.put(child)
        return height

def main():
    tree = TreeHeight()
    tree.read()
    print(tree.compute_height())

threading.Thread(target=main).start()