class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        rank = defaultdict(int)
        freq = [[] for i in range(len(nums)+1)]

        for i in nums:
            rank[i] += 1

        for i,v in rank.items():
            freq[v].append(i)

        output = []
        for i in range(len(nums), 0 ,-1):
            for j in freq[i]:
                if len(output) == k:
                    break
                output.append(j)

        return output

