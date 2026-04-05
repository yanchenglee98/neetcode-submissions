class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for c in s:
            print(c)
            if c == '(' or c == '{' or c == '[':
                st.append(c)
                continue
            if not st: return False
            c1 = st.pop()
            print(c, c1)
            if c == ')' and c1 != '(':
                return False
            elif c == '}' and c1 != '{':
                return False
            elif c == ']' and c1 != '[':
                return False
        return True if len(st) == 0 else False
