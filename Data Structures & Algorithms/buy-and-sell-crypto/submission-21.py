class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        output = 0
        j = 0

        for i in range(len(prices)):

            if prices[i] < prices[j]:
                j = i

            output = max(output,prices[i] - prices[j])
    
        return output