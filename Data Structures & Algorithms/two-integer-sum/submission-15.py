class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        diffs = defaultdict(int)
        
        for i,n in enumerate(nums):
            diff = target - n
            if diff in diffs:
                return [diffs[diff],i]
            diffs[n] = i
