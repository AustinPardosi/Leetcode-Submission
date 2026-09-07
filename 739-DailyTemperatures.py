class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # stack of the index
        result = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            while len(stack) != 0 and temp > temperatures[stack[-1]]:
                top = stack.pop()
                result[top] = i - top
            stack.append(i)
        return result