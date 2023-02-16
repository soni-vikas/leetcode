# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        queue = []
        if root:
            queue = [root]

        while queue:
            temp_queue = []
            right_most = None

            while queue:
                front = queue.pop(0)
                right_most = front.val
                if front.left:
                    temp_queue.append(front.left)

                if front.right:
                    temp_queue.append(front.right)

            queue = temp_queue
            ans.append(right_most)

        return ans
