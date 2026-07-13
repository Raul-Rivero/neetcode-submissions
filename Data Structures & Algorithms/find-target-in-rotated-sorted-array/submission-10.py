class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l,r = 0,len(nums) - 1

        while l <= r:

            m = (l + r) // 2
            if nums[m] == target:
                return m

            # pointer fell on the left sorted side
            if nums[m] >= nums[l]:
                #check whether the target is between m and l
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1

            #pointer fell on the right side
            else:
                if target > nums[r] or target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            
        return -1