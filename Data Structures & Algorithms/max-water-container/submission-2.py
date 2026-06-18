class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        cur = 0

        l = 0
        r = len(heights) - 1

        while l < r:

            if heights[l] < heights[r]:
                height = heights[l]
            else:
                height = heights[r]


            cur = max(cur, height * (r-l))


            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

            # if heights[l] < heights[r]:
            #     height = heights[l]
            # else:
            #     height = heights[r]

            # cur = max(cur, height * (r-l))

        return cur 