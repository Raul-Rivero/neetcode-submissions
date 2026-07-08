class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        cur = max(piles)

        l = 1
        r = max(piles)

        while l <= r:
            k = (l + r) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p/k)
            
            if hours <= h:
                cur = min(cur,k)
                r = k - 1
            else:
                l = k + 1

        return cur

        


