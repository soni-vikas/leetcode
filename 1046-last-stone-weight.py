import heapq
from typing import List


class Solution:
    def get_nonce(self):
        self._nonce += 1
        return self._nonce

    def build_max_heap(self, stones):
        heap = []
        for stone in stones:
            heapq.heappush(heap, (-stone, self.get_nonce()))

        return heap

    def lastStoneWeight(self, stones: List[int]) -> int:
        self._nonce = 0
        heap = self.build_max_heap(stones)

        while len(heap) > 1:
            first = heapq.heappop(heap)[0]
            second = heapq.heappop(heap)[0]
            if first - second:
                heapq.heappush(heap, (-abs(first - second), self.get_nonce()))

        return abs(heap[0][0]) if heap else 0
