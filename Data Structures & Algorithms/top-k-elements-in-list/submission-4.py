class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = defaultdict(int)

        ranked_elems = [[] for i in range(len(nums)+1)]

        for i in nums:
            count[i] += 1

        for key,value in count.items():
            ranked_elems[value].append(key)

        out = []
        for i in range(len(ranked_elems) - 1,0,-1):
            for j in ranked_elems[i]:
                out.append(j)
                if len(out) == k:
                    return out
