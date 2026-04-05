# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head
        slow = head
        i = 0
        while i < n and fast:
            i+=1
            fast = fast.next
        prev = None
        while fast:
            prev = slow
            slow = slow.next
            fast = fast.next
        if not prev:
            return slow.next
        prev.next = slow.next
        return head