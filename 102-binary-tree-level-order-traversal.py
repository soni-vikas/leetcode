# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        queue = []
        if root:
            queue = [root]

        while queue:
            temp_queue = []
            temp_ans = []

            while queue:
                front = queue.pop(0)
                temp_ans.append(front.val)
                if front.left:
                    temp_queue.append(front.left)

                if front.right:
                    temp_queue.append(front.right)

            queue = temp_queue
            ans.append(temp_ans)

        return ans
