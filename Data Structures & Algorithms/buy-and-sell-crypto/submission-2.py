class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prof = 0
        l,r = 0, 1

        while r < len(prices):
            prof = max(prof, (prices[r] - prices[l]))

            if (prices[r] - prices[l] < 0):
                l = r
                r += 1
            else:
                r += 1
        
        return prof
