# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from copy import deepcopy

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        h = deepcopy(head)
        answer = list()
        idx = 0
        while head:
            head = head.next
            idx += 1

        head = deepcopy(h)
        
        if idx == 1:
            head = None
            return head
        if idx == n:
            return head.next
        
        answer = head
        for i in range(idx-n-1): # idx-n(head) : 제거될 Node 바로 앞 Node
            head = head.next
        tail = head.next.next
        head.next = tail
        return answer
