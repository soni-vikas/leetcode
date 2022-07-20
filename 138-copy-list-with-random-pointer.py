"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        temp = head
        while temp:
            new_node = Node(temp.val, temp.next)
            temp.next = new_node
            temp = new_node.next

        def print_head(r):
            ls = []
            while r:
                ls.append(r.val)
                r = r.next

            print(ls)

        temp = head
        new_temp = new_head = None

        while temp:
            if temp.random:
                temp.next.random = temp.random.next

            if new_head is None:
                new_temp = new_head = temp.next

            else:
                new_temp.next = temp.next
                new_temp = new_temp.next

            temp = new_temp.next

        return new_head
