from functools import lru_cache
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp1, dp2 = 1, 1
        for i in range(n-1, -1, -1):
            dp = 0
            if s[i] == '0':
                dp = 0
            else:
                dp = dp1
            if i + 1 < n:
                if s[i] == "1" or (s[i] == "2" and s[i+1] < "7"):
                    dp+=dp2
            dp2 = dp1
            dp1 = dp
        return dp1
        