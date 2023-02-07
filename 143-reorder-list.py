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


def rotate(head):
    prev = None
    while head:
        next = head.next
        head.next = prev
        prev = head
        head = next

    return prev


class Solution:

    def reorderList(self, head1: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        mid = int(get_len(head1) / 2)

        if mid == 0:
            return head1

        # splitting from mid
        prev = None
        curr = head1
        while mid:
            prev = curr
            curr = curr.next
            mid -= 1

        prev.next = None

        # rotating the right subarray
        head2 = rotate(curr)

        # reorder the list by taking element from each halves. 
        res = curr = ListNode(-1)
        while head1:
            curr.next = head1
            head1 = head1.next
            curr.next.next = head2
            head2 = head2.next
            curr = curr.next.next

        curr.next = head2
        return res.next

