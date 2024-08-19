# python3

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeHeight:
        def read(self):
                self.n = int(sys.stdin.readline())
                self.parent = list(map(int, sys.stdin.readline().split()))
                self.node_cache = [0] * self.n
        
        def calculate_depth_of_node(self, node_id):
                parent = self.parent[node_id]
                if parent == -1: # on root
                        return 1
                # case when it is not on the root and not in node_cache
                if self.node_cache[node_id]:
                        return self.node_cache[node_id]
                # else
                self.node_cache[node_id] = 1 + self.calculate_depth_of_node(self.parent[node_id])
                return self.node_cache[node_id]

        def compute_height(self):
                # Replace this code with a faster implementation
                node_list = [self.calculate_depth_of_node(i) for i in range(self.n)]
                return max(node_list)
        

def main():
        tree = TreeHeight()
        tree.read()
        print(tree.compute_height())

threading.Thread(target=main).start()
