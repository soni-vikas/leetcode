import heapq
from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self._nonce = 0
        self.k = k
        self.heap = []
        for val in nums:
            self.add(val)

    def get_nonce(self):
        self._nonce += 1
        return self._nonce

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, (val, self.get_nonce()))
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        
        return self.heap[0][0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
