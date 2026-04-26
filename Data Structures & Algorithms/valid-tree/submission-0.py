# solution
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = set()
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        def dfs(u, prev):
            if u in visited:
                return False
            visited.add(u)
            for v in adj[u]:
                if v == prev: continue
                if not dfs(v, u):
                    return False
            return True
        return dfs(0, None) and len(visited) == n