class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        seen = defaultdict(int)

        for i in nums:
            if seen[i] > 0:
                return True
            seen[i] += 1

        return False