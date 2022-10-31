class Solution:
    #  My understanding
    #   we keep taking sum of elements and keep adding the sum % k value in map .
    #   If at any index i, we see that remainder, that sum(till index i) is giving is already present in map then it means that the subarray which lies between that index(found in map)
    #   and this i has sum multiple of k , why ?, suppose that k = 7 and sum till any index i is 15 (15 % 7 = 1) .. suppose on finding in map we found an element (8, 1) i.e. (8 % 7 == 1)
    #   therefore both the remainders are same i. e. 1, so the subarray which lies in between these 2 sums has sum 15 - 8 = 7 i.e. multiple of k .

    # Why are we inserting (0, -1) at starting ?
    #   take this example : [23, 2, 4, 6, 6] and k = 7 ...
    #   We see that sub-array [23, 2, 4, 6] will have sum 35 so remainder will be 0,
    #   but in order to return this answer we need a condition i.e. element should already be present in the map,
    #   but that condition cannot be satisfied, if we don't insert the base case i.e. (0, -1)

    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        hashmap = {0: -1}
        sum = 0

        for i, n in enumerate(nums):
            sum = (sum + n) % k
            if sum not in hashmap:
                hashmap[sum] = i
            else:
                if i - hashmap[sum] >= 2:
                    return True

        return False
