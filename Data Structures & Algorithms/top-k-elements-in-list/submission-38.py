class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = defaultdict(int)
        reps = [[] for i in range(len(nums)+1)]

        for i in nums:
            freq[i] += 1

        for key,value in freq.items():
            reps[value].append(key)

        output = []

        for i in reps[::-1]:
            for j in i:
                output.append(j)
                if len(output) == k:
                    return output


