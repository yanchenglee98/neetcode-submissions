# hint and use prev solution to find pivot
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l < r:
            m = (l+r)//2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
                
        def bsearch(le,rr):
            print(le,rr)
            while le <= rr:
                m = le + (rr-le)//2
                if nums[m] == target:
                    return m
                elif nums[m] > target:
                    rr = m - 1
                else:
                    le = m + 1
            return -1 
        
        if target > nums[-1]:
            return bsearch(0, l-1)
        elif target < nums[-1]:
            return bsearch(l, len(nums)-1)
        else:
            return len(nums)-1
