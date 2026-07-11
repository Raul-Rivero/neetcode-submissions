class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums) - 1

        while l <= r:

            m = (l + r) // 2
            if nums[m] == target:
                return m


            #check where m is at 

            # m is on the left sorted side (basically when the value @ m
            # is larger than or equal at the value at l
            if nums[m] >= nums[l]:
                # check that the target is between l and m
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1

            # m is on the right sorted side
            else:
                # check if the target is between m and r
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1

        return -1