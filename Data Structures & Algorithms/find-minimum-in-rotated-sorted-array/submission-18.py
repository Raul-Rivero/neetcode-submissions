class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        cur = nums[0]

        l,r = 0,len(nums)-1

        while l <= r:
            if nums[l] < nums[r]:
                cur = min(cur,nums[l])
                return cur
            
            m = (l + r) // 2
            cur = min(cur,nums[m])

            if nums[m] >= nums[r]:
                l = m + 1
            else:
                r = m - 1
            
        return cur