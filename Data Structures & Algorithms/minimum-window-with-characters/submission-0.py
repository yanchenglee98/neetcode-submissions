# chatgpt help
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        need_count = len(need)
        have = 0
        l = 0
        window = Counter()
        res = ""
        res_length = float('inf')
        for r in range(len(s)):
            char = s[r]
            if char in need:
                window[char]+=1
                if window[char] == need[char]:
                    have+=1
            while have == need_count:
                if (r-l+1) < res_length:
                    res = s[l:r+1]
                    res_length = r-l+1
                if s[l] in need:
                    window[s[l]]-=1
                    if window[s[l]] < need[s[l]]:
                        have-=1
                l+=1
        return res        
        