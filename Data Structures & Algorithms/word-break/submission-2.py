class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        hm = {}
        def dfs(i):
            if i in hm:
                return hm[i]
            if i >= len(s):
                return True
            res = False
            for word in wordDict:
                j = len(word)
                print(word, s[i:i+j], i+j)
                if i+j <= len(s) and s[i:i+j] == word:
                    res = res or dfs(i+j)
                else:
                    res = res or False
            hm[i] = res
            return res
        return dfs(0)
        