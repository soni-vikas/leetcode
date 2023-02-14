# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"{self.val} -> {self.next}"


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        res = None
        prev = None
        curr = head
        while curr:
            curr = self.reverse(curr, k)
            res = res or curr
            if prev:
                prev.next = curr

            i = 0
            while i < k and curr:
                prev = curr
                curr = curr.next
                i += 1

        return res

    @classmethod
    def reverse(cls, head, k):
        prev = None
        curr = head
        while curr and k:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            k -= 1

        head.next = curr
        return prev


if __name__ == '__main__':
    def get_ll(ls):
        temp = head = ListNode(-1)
        for i in ls:
            temp.next = ListNode(i)
            temp = temp.next

        return head.next


    for ls, k in [
        ([1, 2, 3, 4, 5], 2),
        ([1, 2, 3, 4, 5], 3),
        ([1, 2, 3, 4, 5], 4),
        ([1, 2, 3, 4, 5], 5),
        ([1, 2, 3, 4, 5], 6),
        ([1, 2, 3, 4, 5], 1),
        ([], 1),
    ]:
        print(Solution().reverseKGroup(get_ll(ls), k))
