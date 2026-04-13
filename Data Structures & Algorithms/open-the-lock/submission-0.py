#https://leetcode.com/problems/open-the-lock/?envType=daily-question&envId=2024-04-22
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        queue = deque()
        queue.append("0000")
        depth = 0
        visited = set(deadends)
        while queue:
            size = len(queue)
            for _ in range(size):
                s = queue.popleft()
                if s == target:
                    return depth
                if s in visited: continue
                visited.add(s)
                queue.extend(self.successors(s))
            depth+=1
        return -1

    
    def successors(self, src):
        res = []
        for i, ch in enumerate(src):
            num = int(ch)
            res.append(src[:i] + str((num+1) % 10) + src[i+1:])
            res.append(src[:i] + str((num-1) % 10) + src[i+1:])
        return res