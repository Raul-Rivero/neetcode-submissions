class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        output = []

        l = 0
        r = l + k

        while r < len(nums) + 1:
            output.append(max(nums[l:r]))
            l += 1
            r = l + k

        return output