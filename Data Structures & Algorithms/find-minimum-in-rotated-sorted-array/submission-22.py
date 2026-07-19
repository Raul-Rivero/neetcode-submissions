class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        cur = nums[0]

        l,r = 0, len(nums) - 1

        while l <= r:
            if nums[l] < nums[r]:
                return min(cur, nums[l])
            
            m = (l + r) // 2
            cur = min(cur,nums[m])

            if nums[m] < nums[l]:
                r = m - 1
            else:
                l = m + 1

        return cur
