"""
Basics Functions of a binary heap
"""
from abc import ABC, abstractmethod
import math


class BinaryHeap(ABC):
    def __init__(self):
        self.heap = []

    def insert(self, k):
        self.heap.append(k)
        # do bubble up
        self.bubble_up(len(self.heap)-1)

    def delete_root(self):
        self.heap[0] = self.heap[-1]
        del self.heap[-1]
        self.sift_down(0)

    @abstractmethod
    def bubble_up(self, pos):
        pass

    @abstractmethod
    def sift_down(self, pos):
        pass


class MinHeap(BinaryHeap):
    def bubble_up(self, pos):
        parent = math.floor(pos/2)
        if self.heap[parent] > self.heap[pos]:
            temp = self.heap[parent]
            self.heap[parent] = self.heap[pos]
            self.heap[pos] = temp
            self.bubble_up(parent)
        return

    def sift_down(self, pos):
        left_child = 2*pos
        right_child = 2*pos+1
        # Decide which leaf to check
        if left_child >= len(self.heap) and right_child >= len(self.heap):
            return
        elif right_child >= len(self.heap):
            target = left_child
        else:
            target = right_child if min(self.heap[right_child], self.heap[left_child]) == self.heap[right_child] else left_child
        if self.heap[target] < self.heap[pos]:
            temp = self.heap[target]
            self.heap[target] = self.heap[pos]
            self.heap[pos] = temp
            self.sift_down(target)


class MaxHeap(BinaryHeap):
    def bubble_up(self, pos):
        parent = math.floor(pos/2)
        if self.heap[parent] < self.heap[pos]:
            temp = self.heap[parent]
            self.heap[parent] = self.heap[pos]
            self.heap[pos] = temp
            self.bubble_up(parent)
        return

    def sift_down(self, pos):
        left_child = 2*pos
        right_child = 2*pos+1
        # Decide which leaf to check
        if left_child >= len(self.heap) and right_child >= len(self.heap):
            return
        elif right_child >= len(self.heap):
            target = left_child
        else:
            target = right_child if max(self.heap[right_child], self.heap[left_child]) == self.heap[right_child] else left_child
        if self.heap[target] > self.heap[pos]:
            temp = self.heap[target]
            self.heap[target] = self.heap[pos]
            self.heap[pos] = temp
            self.sift_down(target)


if __name__ == "__main__":
    test = [5, 11, 23, 3, 2, 85, 1, 95, 1, 2, 67, 1]

    b_heap = MinHeap()
    for i in test[:4]:
        b_heap.insert(i)
    print(b_heap.heap)
    b_heap.delete_root()
    print(b_heap.heap)


    b_heap = MaxHeap()
    for i in test[:4]:
        b_heap.insert(i)
    print(b_heap.heap)
    b_heap.delete_root()
    print(b_heap.heap)

