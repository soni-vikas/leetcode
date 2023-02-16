# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode, so_far_max=-10001) -> int:
        return (
                int(root.val >= so_far_max) +
                self.goodNodes(root.left, max(root.val, so_far_max)) +
                self.goodNodes(root.right, max(root.val, so_far_max))
        ) if root else 0
