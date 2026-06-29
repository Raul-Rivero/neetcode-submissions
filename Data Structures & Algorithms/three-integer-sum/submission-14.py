class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        output = []


        for i,n in enumerate(nums):
            if i > 0 and n == nums[i - 1]:
                continue

            l = i + 1
            r = len(nums) - 1

            while l < r:
                if nums[l] + nums[r] + n < 0:
                    l += 1
                elif nums[l] + nums[r] + n > 0:
                    r -= 1
                else:
                    output.append([nums[l],nums[r],n])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
            
        return output

