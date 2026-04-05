# hint
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        se = set()
        l = 0
        mx = 0
        for i, v in enumerate(s):
            if v in se:
                mx = max(i - l, mx)
                while s[i] in se: 
                    se.remove(s[l])
                    l += 1
            se.add(v)
        if se: mx = max(mx, len(se))
        return mx