class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        output = 0

        l = 0
        r = len(heights) - 1

        while l < r:

            height = min(heights[l],heights[r])

            area = height * (r - l)

            output = max(area,output)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return output