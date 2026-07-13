class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        cur = 0

        l,r = 0, len(heights) - 1

        while l < r:

            area = min(heights[l],heights[r]) * (r - l)
            cur = max(cur,area)

            if heights[r] < heights[l]:
                r -= 1
            else:
                l += 1
        
        return cur