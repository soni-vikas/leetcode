import heapq
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x, y in points:
            heapq.heappush(heap, (-(x ** 2 + y ** 2), x, y))
            if len(heap) > k:
                heapq.heappop(heap)

        return [[x, y] for _, x, y in heap]
