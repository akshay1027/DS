# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Recursive DFS solution
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None

        temp = root.left
        root.left = root.right
        root.right = temp

        self.invertTree(self, root.left)
        self.invertTree(self, root.right)

        return root

    # iterative solution

        # stack=[root]
        # while stack:
        #     node = stack.pop()
        #     if node:
        #         node.left, node.right = node.right, node.left
        #         stack += node.left, node.right
        # return root
