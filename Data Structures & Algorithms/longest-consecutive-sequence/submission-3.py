class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        cur = []

        nums.sort()
        new_nums = []
        for i in nums:
            if i not in new_nums:
                new_nums.append(i)

        print(new_nums)

        i = 0
        j = 0

        while i < len(new_nums):
            temp = [new_nums[i]]
            j = i + 1

            while j < len(new_nums):
                
                if new_nums[j-1]+1 == new_nums[j]:
                    temp.append(new_nums[j])
                    j += 1
                else:
                    if len(temp) > len(cur):
                        cur = temp
                    break
            i = j

            if j >= len(new_nums) and len(temp) > len(cur):
                cur = temp

        print(cur)
        return len(cur)