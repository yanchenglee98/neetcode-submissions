# copied
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        arr = []
        curr = head
        while curr:
            arr.append(curr)
            curr = curr.next
        p1 = 0
        p2 = len(arr)-1
        while p1 < p2:
            arr[p1].next = arr[p2]
            p1+=1
            if p1 >= p2:
                break
            arr[p2].next = arr[p1]
            p2-=1
        arr[p1].next = None