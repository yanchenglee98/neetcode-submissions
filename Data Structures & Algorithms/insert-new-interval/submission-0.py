import bisect
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        intervals.sort()
        ns, ne = newInterval
        for s, e in intervals:
            if e < ns:
                res.append([s,e])
            elif s > ne:
                res.append([s,e])
            else: 
                if e >= ns:
                    ns = min(s, ns)
                if s <= ne:
                    ne = max(e, ne)
        res.append([ns,ne])
        res.sort()
        return res