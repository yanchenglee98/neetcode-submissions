# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        arr = []
        for l in lists:
            c = l
            while c:
                arr.append(c)
                c = c.next
        arr = sorted(arr, key=lambda x: x.val)
        dummy = ListNode()
        curr = dummy
        for i in arr:
            curr.next = i
            curr = curr.next
        return dummy.next
        