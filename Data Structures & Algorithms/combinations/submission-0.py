class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        path = []
        def dfs(i, j):
            if j == k:
                res.append(path[:])
                return
            if i >  n:
                if j == k:
                    res.append(path[:])
                return
            # choose
            path.append(i)
            dfs(i+1, j+1)
            # backtrack
            path.pop()
            # skip
            dfs(i+1, j)
        dfs(1, 0)
        return res