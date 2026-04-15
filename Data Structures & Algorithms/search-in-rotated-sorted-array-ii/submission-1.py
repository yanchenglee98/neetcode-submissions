# hint from ai
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums)-1
        while l <= r:
            m = (l+r) // 2
            left,right,mid = nums[l], nums[r], nums[m]
            if mid == target:
                return True
            if left < mid:
                # left sorted
                if left <= target < mid:
                    r = m-1
                else:
                    l = m+1
            elif left > mid:
                # right sorted
                if mid < target <= right:
                    l = m+ 1
                else:
                    r = m-1
            else:
                l += 1
        return False