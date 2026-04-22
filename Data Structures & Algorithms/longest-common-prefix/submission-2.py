class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest = min(strs)
        for s in strs:
            for i in range(min(len(longest), len(s))):
                if longest[i] != s[i]:
                    longest = longest[:i]
                    break
        return longest