from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def get_len(head):
    l = 0
    while head:
        l += 1
        head = head.next

    return l


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = get_len(head)

        prev = None
        curr = head

        pos = l - n
        while pos:
            prev = curr
            curr = curr.next
            pos -= 1

        if not prev:
            return curr.next

        prev.next = curr.next
        return head
