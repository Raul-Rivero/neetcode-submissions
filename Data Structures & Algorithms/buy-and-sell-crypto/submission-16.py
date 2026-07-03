class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cur = 0

        l = 0 
        for r in range(len(prices)):
            if prices[r] < prices[l]:
                l = r
            cur = max(cur, prices[r] - prices[l])

        return cur