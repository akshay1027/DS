class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # l, r = 0, 1
        # maxProfit = 0

        # while(r < len(prices)):
        #     if(prices[r] > prices[l]):
        #         maxProfit = max(maxProfit, prices[r]-prices[l])
        #     else:
        #         l = r
        #     r += 1

        # return maxProfit

        l = 0
        maxProfit = 0

        for r in range(1, len(prices)):
            if(prices[r] < prices[l]):
                l = r

            maxProfit = max(maxProfit, prices[r]-prices[l])

        return maxProfit
