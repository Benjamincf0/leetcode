class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        out = [0] * len(temperatures)

        for i, n in enumerate(temperatures).__iter__():
            while stack and stack[-1][0] < n:
                numDays = i - stack[-1][1]
                out[stack[-1][1]] = numDays
                stack.pop()
            
            stack.append((n, i))
        
        return out