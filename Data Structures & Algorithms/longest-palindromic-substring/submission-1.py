class Solution:
    def longestPalindrome(self, s: str) -> str:
        def isPalindrome(i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i+=1
                j-=1
            return True
        res = s[0]

        for i in range(len(s)-1):
            for j in range(len(s)):
                if isPalindrome(i, j) and (j-i+1) > len(res):
                    res = s[i:j+1]
        return res
        