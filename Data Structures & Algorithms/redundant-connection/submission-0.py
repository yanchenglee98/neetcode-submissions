class DSU:
    def __init__(self):
        self.hm = {}
    def find(self, x):
        if x not in self.hm:
            self.hm[x] = x
        if self.hm[x] != x:
            self.hm[x] = self.find(self.hm[x])
        return self.hm[x]
    def union(self, x, y):
        self.hm[self.find(x)] = self.find(y)

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = DSU()
        for a, b in edges:
            if uf.find(a) == uf.find(b):
                return [a, b]
            uf.union(a, b)
            