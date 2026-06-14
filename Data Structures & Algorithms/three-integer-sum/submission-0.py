class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_list = sorted(nums)
        output = []

        for i,a in enumerate(sorted_list):
            if i > 0 and sorted_list[i-1] == a:
                continue

            l = i + 1
            r = len(sorted_list)-1

            while l < r:
                threeSum = a + sorted_list[l] + sorted_list[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    output.append([a,sorted_list[l],sorted_list[r]])
                    l += 1
                    while sorted_list[l] == sorted_list[l - 1] and l < r:
                        l += 1

        return output