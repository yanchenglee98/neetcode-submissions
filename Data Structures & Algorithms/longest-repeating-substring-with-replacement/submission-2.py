class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        se = set(s)
        res = 0
        for c in se:
            print(c)
            count, l = 0, 0
            for i , v in enumerate(s):
                if v != c:
                    count += 1
                print(l, i)
                while count > k:
                    if s[l] != c: count-=1
                    l+=1
                res = max(i-l+1, res)
        return res