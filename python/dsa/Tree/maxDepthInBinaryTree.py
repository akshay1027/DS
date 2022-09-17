class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    def maxDepth1(self, root: TreeNode) -> int:
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
                # print(q)
            level += 1

        return level

    def maxDepthDFS(self, root) -> int:
        level = 0
        stack = [[root, 1]]

        while stack:
            node, depth = stack.pop()
            if node:
                level = max(level, depth)
                stack.append([node.right, depth+1])
                stack.append([node.left, depth+1])
        return level
