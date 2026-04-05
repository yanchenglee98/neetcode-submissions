class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjlist = defaultdict(list)
        indegree = [0 for _ in range(numCourses)]
        for a, b in prerequisites:
            adjlist[b].append(a)
            indegree[a]+=1
        
        queue = collections.deque()
        for i, deg in enumerate(indegree):
            if deg == 0:
                queue.append(i)
        taken = []
        while queue:
            course = queue.popleft()
            taken.append(course)
            for nxt in adjlist[course]:
                indegree[nxt]-=1
                if indegree[nxt] == 0:
                    queue.append(nxt)
        return len(taken) == numCourses