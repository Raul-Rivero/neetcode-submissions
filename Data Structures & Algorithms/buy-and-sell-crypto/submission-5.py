class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        

        cur = 0

        i = 0
        j = 1

        while j < len(prices):
            if prices[j] < prices[i]:
                i = j
            cur = max(cur, prices[j] - prices[i])
            j += 1

        return cur