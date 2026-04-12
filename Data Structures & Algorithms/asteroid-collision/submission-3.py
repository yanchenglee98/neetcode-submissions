class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        res = []
        for ast in asteroids:
            if ast > 0:
                stack.append(ast)
            else:
                isExploded = False
                while stack:
                    if stack[-1] < abs(ast):
                        stack.pop()
                    elif stack[-1] > abs(ast):
                        isExploded = True
                        break
                    else:
                        isExploded = True
                        stack.pop()
                        break
                if not isExploded:
                    res.append(ast)
        return res + stack