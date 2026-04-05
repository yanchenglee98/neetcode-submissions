# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        carry = 0
        curr = dummy
        while l1 or l2:
            s = carry
            if l1: s+=l1.val
            if l2: s+=l2.val
            carry = s // 10
            curr.next = ListNode(s % 10)
            curr = curr.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        if carry:
            curr.next = ListNode(carry)
        return dummy.next