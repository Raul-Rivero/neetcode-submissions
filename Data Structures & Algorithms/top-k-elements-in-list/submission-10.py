class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        

        freq = defaultdict(int)

        res = [[] for i in range(len(nums)+1)]

        for i in nums:
            freq[i] += 1

        for key,value in freq.items():
            res[value].append(key)

        output = []
        for i in range(len(res)-1,0,-1):
            for j in res[i]:
                output.append(j)
                if len(output) == k:
                    return output
  



