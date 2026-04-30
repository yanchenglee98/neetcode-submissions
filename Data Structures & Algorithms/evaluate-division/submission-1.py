# hint https://leetcode.com/problems/evaluate-division/submissions/1952701447/
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(list)
        for i in range(len(equations)):
            a, b = equations[i]
            val = values[i]
            adj[a].append((b, val))
            adj[b].append((a, 1/val))
        res = []
        for i, query in enumerate(queries):
            c, d = query
            if c not in adj or d not in adj: 
                res.append(-1.0)
                continue
            visited = set()
            queue = deque()
            queue.append((c, 1.0))
            isAns = False
            
            while queue:
                curr, mult = queue.popleft()
                visited.add(curr)
                if curr == d:
                    isAns = True
                    res.append(mult)
                    break
                for neighbour, val in adj[curr]:
                    if neighbour in visited: continue
                    queue.append((neighbour, mult * val))
            if not isAns: res.append(-1.0)
        return res