import heapq
from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals)

        heap = []
        res = 0
        for i, j in intervals:
            while heap and heap[0][0] <= i:
                heapq.heappop(heap)

            heapq.heappush(heap, (j, i))
            res = max(res, len(heap))

        return res
