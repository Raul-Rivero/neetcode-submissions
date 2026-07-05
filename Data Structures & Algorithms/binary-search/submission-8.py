class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l,r = 0, len(nums) - 1

        while l <= r:
            center_val = (r + l) // 2

            if target > nums[center_val]:
                l = center_val + 1
            elif target < nums[center_val]:
                r = center_val - 1
            else:
                return center_val

        return -1