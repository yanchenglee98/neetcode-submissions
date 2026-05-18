class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        p1, p2 = 0, 0
        n, m = len(word1), len(word2)
        while p1<n and p2<m:
            if p1 <= p2:
                res.append(word1[p1])
                p1+=1
            else:
                res.append(word2[p2])
                p2+=1
        res = "".join(res)
        if p1 <n:
            res+=word1[p1:]
        if p2<m:
            res+=word2[p2:]
        return res
        