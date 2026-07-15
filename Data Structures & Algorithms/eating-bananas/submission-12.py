class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        cur = max(piles)

        l = 1
        r = cur

        while l <= r:
            k = (l + r) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p/k)

            print(hours,k)

            if hours > h:
                l = k + 1
            else:
                cur = min(cur,k)
                r = k - 1

        return cur 

        
            
