class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if self.isNumber(t):
                stack.append(t)
                continue
            v2 = int(stack.pop())
            v1 = int(stack.pop())
            if t == '+':
                stack.append(v1+v2)
            elif t == '-':
                stack.append(v1-v2)
            elif t == '*':
                stack.append(v1*v2)
            elif t == '/':
                stack.append(v1/v2)
        return int(stack[-1])
    def isNumber(self, s):
        try:
            float(s)
            return True
        except:
            return False
