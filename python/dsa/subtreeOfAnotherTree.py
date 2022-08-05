# https://leetcode.com/problems/subtree-of-another-tree/discuss/102741/Python-Straightforward-with-Explanation-(O(ST)-and-O(S%2BT)-approaches)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # check if root or subRoot is empty. these are edge cases.
        # implement the sameTree function. In base function, decrement root in every recursive call
        # until the base of root and subRoot is same ( only if solution exists)
        if not root:
            return False
        if not subRoot:
            return True

        if self.isSameTree(root, subRoot):
            return True

        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))

    def isSameTree(self, s, sb):
        if not s and not sb:
            return True

        if not s or not sb:
            return False

        if s and sb and s.val == sb.val:
            return (self.isSameTree(s.left, sb.left) and self.isSameTree(s.right, sb.right))
