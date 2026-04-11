class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        res = 0
        l, r = 0, len(people)-1
        mx = max(people)
        freq = [0 for _ in range(mx+1)]
        for p in people:
            freq[p]+=1
        i= 0
        for val, freq in enumerate(freq):
            while freq > 0:
                freq-=1
                people[i] = val
                i+=1
        while l <= r:
            total = people[l] + people[r] if l != r else people[l]
            if total > limit:
                r-=1
                res+=1
            else:
                l+=1
                r-=1
                res+=1
        return res