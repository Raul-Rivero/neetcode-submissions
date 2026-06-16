class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        l = 0 
        r = len(heights)-1

        cur = 0

        while l < r:
            
            if heights[l] < heights[r]:
                height = heights[l]
            else:
                height = heights[r]

            base = abs(l - r)

            tempArea = height*base

            cur = max(cur,tempArea)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
            
        return cur
        

