from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        mem = {v: i for i, v in enumerate(inorder)}
        return self.buildTreeUtil(preorder, inorder, mem, 0, 0, len(preorder))

    def buildTreeUtil(self, preorder: List[int], inorder: List[int], mem, pi, ii, n):
        if n <= 0:
            return None

        idx = mem[preorder[pi]]
        n_left = idx - ii
        n_right = n - n_left - 1
        return TreeNode(
            preorder[pi],
            self.buildTreeUtil(preorder, inorder, mem, pi + 1, ii, n_left),
            self.buildTreeUtil(preorder, inorder, mem, pi + n_left + 1, idx + 1, n_right)
        )
