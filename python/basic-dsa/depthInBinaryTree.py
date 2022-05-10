# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # recursive DFS solution
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    # iterative BFS solution
    def maxDepthBFS(self, root: TreeNode) -> int:
        if not root:
            return 0
        level = 0
        q = deque([root])

        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1

        return level

    def maxDepthDFS(self, root: TreeNode) -> int:
        level = 0
        stack = [[root, 1]]

        while stack:
            node, depth = stack.pop()
            if node:
                level = max(level, depth)
                stack.append([node.right, depth+1])
                stack.append([node.left, depth+1])
        return level
