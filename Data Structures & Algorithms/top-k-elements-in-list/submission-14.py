class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ranks = defaultdict(int)

        freq = [[] for i in range(len(nums)+1)]

        for i in nums:
            ranks[i] += 1

        print(ranks)
        for key,value in ranks.items():
            freq[value].append(key)

        output = []
        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                output.append(n)
                if len(output) == k:
                    return output
