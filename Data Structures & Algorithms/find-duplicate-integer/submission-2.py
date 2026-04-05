# used hint
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            n = nums[i]
            # if we encounter a negative number 
            # it means that a previous n with the same number/index has flipped the value to negative before
            if nums[abs(n)-1] < 0: return abs(n)
            # we use the abs of the n and use n-1 (0-index) to flip the value to negative
            nums[abs(n)-1] = -nums[abs(n)-1]