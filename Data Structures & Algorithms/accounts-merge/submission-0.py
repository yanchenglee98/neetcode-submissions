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
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = DSU()
        hm = {}
        for i, emails in enumerate(accounts):
            for email in emails[1:]:
                if email in hm:
                    uf.union(i, hm[email])
                else:
                    uf.union(email, i)
                    hm[email] = i
        components = defaultdict(list)
        for key in hm.keys():
            idx = uf.find(key)
            components[idx].append(key)
        res = []
        for key, ls in components.items():
            res.append([accounts[key][0]] + ls)
        return res