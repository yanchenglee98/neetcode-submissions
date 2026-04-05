class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hs=set(nums)
        res = 0 
        for i in hs:
            if (i-1) not in hs:
                count = 0
                while i in hs:
                    count+=1
                    i+=1
                res = max(count, res)
        return res