class Solution:

    # not fully correct, passed 45/250 test cases
    def trap(self, height: List[int]) -> int:
        res = 0
        temp = 0

        start = 0  # start of the container
        # move means, the moving part of container or we can say eqaul to breadth
        for move in range(1, len(height)):
            if height[start] > height[move]:
                temp = temp + abs(height[start] - height[move])

            elif height[move] >= height[start]:
                res = res + max(res, temp)
                start = move

        return res
