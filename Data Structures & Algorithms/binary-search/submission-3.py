class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) -1

        while l <= r:
            center = (r + l) // 2
            if nums[center] < target:
                l = center + 1
            elif nums[center] > target:
                r = center - 1
            else:
                return center
        return -1