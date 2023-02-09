# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode], _carry: int = 0) -> Optional[ListNode]:
        if not l1 and not l2:
            return ListNode(_carry) if _carry else None

        l1 = l1 or ListNode(0)
        l2 = l2 or ListNode(0)
        _sum = l1.val + l2.val + _carry
        l1.val = _sum % 10
        l1.next = self.addTwoNumbers(l1.next, l2.next, _sum // 10)
        return l1
