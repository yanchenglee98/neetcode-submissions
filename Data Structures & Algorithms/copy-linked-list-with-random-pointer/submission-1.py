"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        hm = {}
        dummy = Node(0)
        prev = dummy
        while curr:
            hm[curr] = Node(curr.val, None, None)
            prev.next = hm[curr]
            prev = prev.next
            curr = curr.next
        curr = head
        copy = dummy.next

        while curr:
            if curr.random:
                copy.random = hm[curr.random]
            else:
                copy.random = None
            curr = curr.next
            copy = copy.next
        return dummy.next
        

        