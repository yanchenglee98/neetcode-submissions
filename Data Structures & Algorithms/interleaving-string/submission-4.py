from functools import lru_cache
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n = len(s3)
        @lru_cache
        def dfs(i, j, k):
            if k >= n:
                return True
            str1, str2 = False, False
            if i < len(s1) and s1[i] == s3[k]:
                str1 = dfs(i+1, j, k+1)
            if str1: return str1
            if j < len(s2) and s2[j] == s3[k]:
                str2 = dfs(i, j+1, k+1)
            return str2
        if len(s1) + len(s2) != n: return False
        return dfs(0, 0, 0)
