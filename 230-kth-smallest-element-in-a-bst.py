# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        return self.inorder_k_times(root, k, [0])

    def inorder_k_times(self, root, k, count):
        if root:
            res = self.inorder_k_times(root.left, k, count)

            if res is not None:
                return res

            count[0] += 1
            if count[0] == k: return root.val

            return self.inorder_k_times(root.right, k, count)
