# Definition for a binary tree node.
from typing import Optional, Tuple


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        _, _, ans = self.is_valid(root)
        return ans

    def is_valid(self, root: Optional[TreeNode]) -> Tuple[Optional[int], Optional[int], bool]:
        if not root:
            return None, None, True

        lmi, lmx, is_valid = self.is_valid(root.left)
        if not is_valid or (lmx and lmx >= root.val):
            return None, None, False

        rmi, rmx, is_valid = self.is_valid(root.right)
        if not is_valid or (rmi and rmi <= root.val):
            return None, None, False

        return (
            min(i for i in [lmi, lmx, root.val] if i is not None),
            max(i for i in [rmi, rmx, root.val] if i is not None),
            True
        )
