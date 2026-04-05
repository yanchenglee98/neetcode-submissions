# hint
class TimeMap:

    def __init__(self):
        self.hm= defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hm[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        ls = self.hm[key]
        res = ""
        l, r = 0, len(ls)-1
        while l <= r:
            m = l + (r-l)//2
            if ls[m][0] <= timestamp:
                res = ls[m][1]
                l = m+1
            else:
                r = m-1
        return res #ls[r][1] if ls[r][0] <= timestamp else ""
