class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        for i in numbers:
            diff = target - i
            if diff in numbers and diff > i:
                return[numbers.index(i)+1,numbers.index(diff)+1]