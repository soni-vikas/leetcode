from typing import List, Optional
import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        count = 0
        for node in lists:
            if node:
                heapq.heappush(heap, (node.val, count, node))
                count += 1

        head = tail = ListNode(-1)
        while heap:
            tail.next = heapq.heappop(heap)[2]
            tail = tail.next
            if tail.next:
                heapq.heappush(heap, (tail.next.val, count, tail.next))
                count += 1

        return head.next
