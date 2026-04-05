class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c1 = Counter(s1)
        n = len(s2)
        for i in range(n):
            for j in range(i+1,n+1):
                c2 = Counter(s2[i:j])
                if c2 == c1:
                    return True
        return False
        