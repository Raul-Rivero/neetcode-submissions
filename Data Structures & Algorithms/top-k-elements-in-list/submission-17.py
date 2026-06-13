class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        rank = defaultdict(int)

        freq = [[] for i in range(len(nums)+1)]

        for i in nums:
            rank[i] += 1

        for key, value in rank.items():
            freq[value].append(key)

        print(freq)

        output = []
        for i in range(len(nums),0,-1):
            for j in freq[i]:
                output.append(j)
            if len(output) == k:
                return output