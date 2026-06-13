class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # for i in numbers:
        #     diff = target - i
        #     if diff in numbers and diff > i:
        #         return[numbers.index(i)+1,numbers.index(diff)+1]

        i = 0
        
        while i < len(numbers):
            diff = target - numbers[i]
            j = len(numbers)-1

            while numbers[j] != diff and j > -1:
                j -= 1

            if numbers[j] == diff:
                return [i+1, j+1]
            
            i += 1
            