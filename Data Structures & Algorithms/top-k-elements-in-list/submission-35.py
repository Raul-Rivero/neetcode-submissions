class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = defaultdict(int)
        ranks = [[] for i in range(len(nums)+1)]

        for i in nums:
            freq[i] += 1
    
        for key,value in freq.items():
            ranks[value].append(key)

        output = []
        
        for i in range(len(ranks) - 1,0,-1):
            for j in ranks[i]:
                output.append(j)
                if len(output) == k:
                    return output
                

