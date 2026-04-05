class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        subset = []
        def dfs(open, close):
            if open == n == close:
                s = "".join(subset)
                res.append(s)
                return
            # include open 
            if open < n:
                subset.append('(')
                dfs(open+1, close)
                subset.pop()

            # include close 
            if close < open:
                subset.append(')')
                dfs(open, close+1)
                subset.pop()
        dfs(0, 0)
        return res
        