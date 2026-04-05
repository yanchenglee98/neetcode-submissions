class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        sub = []
        def isPalindrome(i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i+=1
                j-=1
            return True
            
        def dfs(j, i):
            if i >= len(s):
                if j == len(s):
                    res.append(sub[:])
                return

            # partition
            if isPalindrome(j, i):
                sub.append(s[j:i+1])
                dfs(i+1, i+1)
                sub.pop()
            
            # skip partition
            dfs(j, i+1)
        dfs(0,0)
        return res