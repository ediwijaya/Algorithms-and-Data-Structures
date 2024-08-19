# python3
import math
import random

class HeapBuilder:
    def __init__(self):
        self._swaps = []
        self._data = []

    def read_data(self, data):
        # n = int(input())
        self._data = data
        self._size = len(self._data)
        # assert n == len(self._data)

    def write_response(self):
        print(len(self._swaps))
        for swap in self._swaps:
            print(swap[0], swap[1])

    def parent(self, i):
        return math.floor((i - 1)/2)
    
    def left_child(self, i):
        return 2*i + 1
    
    def right_child(self, i):
        return 2*i + 2
    
    def sift_up(self, i):
        while i > 0 and self._data[self.parent(i)] > self._data[i]:
            self._swaps.append((self.parent(i), i))
            self._data[i], self._data[self.parent(i)] = self._data[self.parent(i)], self._data[i]
            i = self.parent(i)

    def generate_swaps(self):
        n = len(self._data)
        for i in range(n):
            self.sift_up(n - (i+1))

    def GenerateSwaps(self):
        for i in range(len(self._data)):
            for j in range(i + 1, len(self._data)):
                if self._data[i] > self._data[j]:
                    self._swaps.append((i, j))
                    self._data[i], self._data[j] = self._data[j], self._data[i]

    def solve_naive(self, data):
        self.read_data(data)
        self.GenerateSwaps()
        # self.write_response()
    
    def solve(self, data):
        self.read_data(data)
        self.generate_swaps()
        # self.write_response()

def stress_test(N, M):
    while True:
        n = random.randint(2, N)
        A = list(random.randint(0, M) for r in range(n))
        print(A)
        builder_naive = HeapBuilder()
        builder_naive.solve_naive(A)
        result_naive = builder_naive._data
        builder_efficient = HeapBuilder()
        builder_efficient.solve(A)
        result_fast = builder_efficient._data
        if result_naive == result_fast:
            print(f"OK: {result_naive}, {result_fast}")
        else:
            print(f"Wrong answer: {result_naive}, {result_fast}")
            break

if __name__ == '__main__':
    stress_test(10, 10)
