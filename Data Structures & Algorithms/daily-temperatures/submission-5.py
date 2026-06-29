class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        count = [0] * len(temperatures)
        stack = [] #[index,temp]

        for i,t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT,stackInd = stack.pop()
                count[stackInd] = i - stackInd
            stack.append([t,i])
        return count