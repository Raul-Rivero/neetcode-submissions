class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l,r = 0,len(nums)-1

        while l <= r:
            if nums[l] <= nums[r]:
                res = min(res, nums[l])
                return res

            m = (r + l) // 2

            if nums[m] >= nums[l]:
                l = m + 1
            else:
                res = nums[m]
                r = m - 1

        return res