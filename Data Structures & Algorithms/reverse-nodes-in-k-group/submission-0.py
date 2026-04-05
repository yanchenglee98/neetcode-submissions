# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        arr = []
        curr = head
        dummy = ListNode()
        prev = dummy
        while curr:
            if len(arr) == k:
                nxt = arr[-1].next
                arr[-1].next = None
                reverse = self.reverse(arr[0])
                arr[0].next = nxt
                curr = nxt
                prev.next = arr[-1]
                prev = arr[0]
                arr = []
            else:
                arr.append(curr)
                curr = curr.next
        if len(arr) == k:
                nxt = arr[-1].next
                arr[-1].next = None
                reverse = self.reverse(arr[0])
                arr[0].next = nxt
                curr = nxt
                prev.next = arr[-1]
                prev = arr[0]
                arr = []
        return dummy.next


    
    def reverse(self, node: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = node
        while curr:
            nxt = curr.next 
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
