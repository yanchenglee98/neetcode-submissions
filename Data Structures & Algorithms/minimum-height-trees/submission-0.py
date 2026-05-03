class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        heights = defaultdict(list)
        def dfs(i, prev):
            mx =  0
            for neighbour in adj[i]:
                if neighbour == prev:
                    continue
                mx = max(mx, 1+dfs(neighbour, i))
            return mx
        for i in range(n):
            h = dfs(i, None)
            heights[h].append(i)
        for h in sorted(heights.keys()):
            return heights[h]