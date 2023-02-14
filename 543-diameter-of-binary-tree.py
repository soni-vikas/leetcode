# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        m = {"max": 0}
        self.diameterOfBinaryTreeUtil(root, m)
        return m["max"]

    def diameterOfBinaryTreeUtil(self, root, m):
        if not root:
            return 0

        lh = self.diameterOfBinaryTreeUtil(root.left, m)
        rh = self.diameterOfBinaryTreeUtil(root.right, m)
        m["max"] = max(lh + rh, m["max"])

        return 1 + max(lh, rh)
