# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        _, is_balanced = self.get_height(root)
        return is_balanced

    def get_height(self, root):
        if not root:
            return 0, True

        lh, is_balanced = self.get_height(root.left)
        if not is_balanced:
            return 0, False

        rh, is_balanced = self.get_height(root.right)
        if not is_balanced:
            return 0, False

        return 1 + max(rh, lh), abs(rh - lh) < 2
