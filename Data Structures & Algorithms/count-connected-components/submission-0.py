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
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = DSU()
        for u, v in edges:
            uf.union(u, v)
        components = set()
        for u in range(n):
            components.add(uf.find(u))
        return len(components)