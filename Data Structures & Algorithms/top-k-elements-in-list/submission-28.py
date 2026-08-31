class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        groups = defaultdict(int)
        freq = [[] for i in range(len(nums) + 1)]

        for i in nums:
            groups[i] += 1
        
        for key,value in groups.items():
            freq[value].append(key)

        output = []

        for i in range(len(freq) -1,-1,-1):
            for j in freq[i]:
                output.append(j)
                if len(output) == k:
                    return output