class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0 for _ in range(len(temperatures))]
        for i, v in enumerate(temperatures):
            if stack and stack[-1][1] > v:
                stack.append((i, v))
            else:
                while stack and stack[-1][1] < v:
                    i2, v2 = stack.pop()
                    res[i2] = i - i2
                stack.append((i,v))
        return res

        