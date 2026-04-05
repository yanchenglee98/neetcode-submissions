# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        idx = 1
        dummy = ListNode(0, head)
        curr = dummy.next
        before = dummy
        while idx != left:
            before = curr
            curr = curr.next 
            idx += 1
        prev = None
        start = curr
        while idx != right+1:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            idx += 1
        before.next = prev
        start.next = curr
        return dummy.next