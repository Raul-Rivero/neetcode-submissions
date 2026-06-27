class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        cur = 0

        l = 0
        r = 0

        while r < len(prices):
            if prices[r] < prices[l]:
                l = r
            
            cur = max(cur, prices[r] - prices[l])

            r += 1

        return cur