class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        reps = defaultdict(int)

        values = [[] for i in range(len(nums)+1)]

        for i in nums:
            reps[i] += 1

        for key,value in reps.items():
            values[value].append(key)
        
        output = []
        for i in range(len(values) - 1, -1, -1):
            for j in values[i]:
                output.append(j)
                if len(output) == k:
                    print(output)
                    return output
        

                    