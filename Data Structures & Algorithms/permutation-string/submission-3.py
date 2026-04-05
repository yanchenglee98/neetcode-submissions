class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c1 = Counter(s1)
        n = len(s2)
        for i in range(n):
            c2 = Counter(s2[i:i+len(s1)])
            if c2 == c1:
                return True
        return False
        