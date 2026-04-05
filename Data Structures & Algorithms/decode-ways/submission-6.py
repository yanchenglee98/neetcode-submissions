from functools import lru_cache
class Solution:
    def numDecodings(self, s: str) -> int:
        hm = {}
        def dfs(i):
            if i in hm:
                return hm[i]
            if i == len(s):
                return 1
            if s[i] == '0':
                return 0
            res = dfs(i+1)
            if i < len(s)-1:
                if s[i]=='1' or (s[i]=='2' and s[i+1] < '7'):
                    res+=dfs(i+2)
            hm[i] = res
            return res

        return dfs(0)
        