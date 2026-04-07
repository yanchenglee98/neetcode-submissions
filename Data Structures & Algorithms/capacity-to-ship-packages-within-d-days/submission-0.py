class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def isValid(cap):
            req = 0
            curr = 0
            for w in weights:
                if curr + w > cap:
                    req+=1
                    curr = w
                else:
                    curr+=w
            if curr > 0: req+=1
            return req <= days
        l = max(weights)
        r = sum(weights)
        while l <= r:
            m = (l+r)//2
            print(l, r, m, isValid(m))
            if isValid(m):
                r = m-1
            else:
                l = m+1
        return l