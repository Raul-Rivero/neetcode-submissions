class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        numbers = defaultdict(int)

        for i,j in enumerate(nums):
            diff = target - j
            if diff in numbers:
                return [numbers[diff],i]
            numbers[j] = i
