class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        cur = max(piles)
        
        #define possible rates
        l,r = 1, max(piles)

        while l <= r:

            m = (l + r) // 2
            k = 0
            for p in piles:
                k += math.ceil(p/m)
            
            if k > h:
                l = m + 1
            else:
                r = m - 1
                cur = min(cur,m)
        
        return cur

