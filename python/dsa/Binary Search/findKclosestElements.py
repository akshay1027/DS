class Solution:
    def findClosestElements(self, A: List[int], k: int, x: int) -> List[int]:

        left, right = 0, len(A) - k
        while left < right:
            mid = (left + right) // 2
            if x - A[mid] > A[mid + k] - x:
                left = mid + 1
            else:
                right = mid
        return A[left:left + k]

    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        ind = -1
        for i in range(len(arr)):
            if arr[i] == x:
                ind = i
                break

        if ind != -1:

            extra = abs((ind - k) + 1)
            ans = []
            tmp = ind+1
            while(ind < 0):
                ans.append(arr[ind])
                ind -= 1

            if extra > 0:
                while(ind < 0):
                    ans.append(arr[tmp])
                    tmp += 1
                    ind -= 1

            ans = sorted(ans)
            return ans

            # if value of x is less than 0
        # else:
        #     if x < arr[]
        #     while(i < k):
        #         ans.append(arr[i])
        #         i += 1
