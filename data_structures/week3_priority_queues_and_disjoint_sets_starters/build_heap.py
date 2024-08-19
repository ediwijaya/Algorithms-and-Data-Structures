# python3
import math

class HeapBuilder:
    def __init__(self):
        self._swaps = []
        self._data = []

    def read_data(self):
        n = int(input())
        self._data = [int(s) for s in input().split()]
        self._size = len(self._data) - 1
        assert n == len(self._data)

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
    
    def extract_min(self):
        result = self._data[0]
        self._data[self._size] = self._data[0]
        self._size -= 1
        self.sift_down(1)
        return result
    
    def insert(self, val):
        self._size += 1
        self._data[self._size] = val
        self.sift_up(self._data)

    def remove(self, val):
        self._data[val] = float('-inf')
        self.sift_up()
        self.extract_min()
    
    def sift_up(self, i):
        while i > 0 and self._data[self.parent(i)] > self._data[i]:
            self._swaps.append((self.parent(i), i))
            self._data[i], self._data[self.parent(i)] = self._data[self.parent(i)], self._data[i]
            i = self.parent(i)

    def sift_down(self, i):
        max_idx = i
        left = self.left_child(i)
        if left <= self._size and self._data[left] < self._data[max_idx]:
            max_idx = left
        right = self.right_child(i)
        if right <= self._size and self._data[right] < self._data[max_idx]:
            max_idx = right
        if i != max_idx:
            self._swaps.append((i, max_idx))
            self._data[max_idx], self._data[i] = self._data[i], self._data[max_idx]
            self.sift_down(max_idx)

    def generate_swaps(self):
        n = len(self._data)
        for i in reversed(range(n)):
            # self.sift_up(i)
            self.sift_down(i)

    def solve(self):
        self.read_data()
        self.generate_swaps()
        self.write_response()

if __name__ == '__main__':
    heap_builder = HeapBuilder()
    heap_builder.solve()