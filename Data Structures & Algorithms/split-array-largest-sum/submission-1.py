#https://neetcode.io/problems/split-array-largest-sum/solution
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def canSplit(largest):
            numSplit = 1
            currSum = 0
            for n in nums:
                if currSum + n > largest:
                    numSplit+=1
                    currSum = n
                    if numSplit > k:
                        return False
                else:
                    currSum+=n
            return True
        l, r = max(nums), sum(nums)
        res = r
        while l <= r:
            m = (l+r)//2
            if canSplit(m):
                res = r
                r = m-1
            else:
                l = m+1
        return l