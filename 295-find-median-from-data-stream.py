import heapq

INFINITY = 10 ** 5 + 1


class MinHeap:
    def __init__(self, *values):
        self.heap = []
        for v in values:
            self.push(v)

    def push(self, i):
        heapq.heappush(self.heap, i)

    def pop(self):
        return heapq.heappop(self.heap)

    def top(self):
        return self.heap[0]

    def len(self):
        return len(self.heap)

    def __repr__(self):
        return " -> ".join([str(i) for i in self.heap])


class MaxHeap:
    def __init__(self, *values):
        self.heap = []
        self.nonce = 0
        for v in values:
            self.push(v)

    def push(self, i):
        heapq.heappush(self.heap, -i)

    def pop(self):
        return -(heapq.heappop(self.heap))

    def top(self):
        return -self.heap[0]

    def len(self):
        return len(self.heap)

    def __repr__(self):
        return " -> ".join([str(-i) for i in self.heap])


class MedianFinder:

    def __init__(self):
        self.left_max_heap = MaxHeap(-INFINITY)
        self.right_min_heap = MinHeap(INFINITY)

    def addNum(self, num: int) -> None:
        if num > self.right_min_heap.top():
            self.right_min_heap.push(num)
            if self.right_min_heap.len() > self.left_max_heap.len():
                self.left_max_heap.push(self.right_min_heap.pop())

        else:
            self.left_max_heap.push(num)
            if self.left_max_heap.len() - self.right_min_heap.len() > 1:
                self.right_min_heap.push(self.left_max_heap.pop())

    def findMedian(self) -> float:
        if self.left_max_heap.len() > self.right_min_heap.len():
            return self.left_max_heap.top()

        return (self.left_max_heap.top() + self.right_min_heap.top()) / 2


if __name__ == '__main__':
    obj = MedianFinder()
    obj.addNum(-1)
    obj.addNum(-2)
    obj.addNum(-3)
    param_2 = obj.findMedian()
    print(param_2 == -2)

    obj = MedianFinder()
    obj.addNum(1)
    obj.addNum(2)
    param_2 = obj.findMedian()
    print(param_2 == 1.5, param_2)
