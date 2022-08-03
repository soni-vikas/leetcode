# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        q = [root]
        ans = ""
        while q:
            root = q.pop(0)
            if root is not None:
                q.append(root.left)
                q.append(root.right)

            ans += f"{'.' if root is None else root.val} "

        return ans.rstrip(" ")

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        data = data.split(" ")

        def get_next_node():
            val = data.pop(0)
            return None if val == "." else TreeNode(val)

        root = get_next_node()
        queue = [root]
        while queue:
            temp = []
            for node in queue:
                if node:
                    node.left = get_next_node()
                    node.right = get_next_node()
                    temp.append(node.left)
                    temp.append(node.right)

            queue = temp

        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
