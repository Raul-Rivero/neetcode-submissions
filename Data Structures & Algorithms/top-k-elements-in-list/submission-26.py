class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        groups = defaultdict(int)

        reps = [[] for i in range(len(nums) + 1)]

        for i in nums:
            groups[i] += 1

        for key, value in groups.items():
            reps[value].append(key)


        output = []
        for i in range(len(reps) - 1, -1, -1):
            for j in reps[i]:
                output.append(j)
                if len(output) == k:
                    return output

