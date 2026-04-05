# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = 0
        curr = head
        while curr:
            l+=1
            curr = curr.next
        print(l)
        l = l-n-1
        i = 0
        curr = head
        if l < 0:
            return curr.next
        while i < l:
            print(i)
            i+=1
            curr = curr.next
        curr.next = curr.next.next
        return head