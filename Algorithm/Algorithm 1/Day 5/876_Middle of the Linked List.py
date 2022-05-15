# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math
from copy import deepcopy

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        h = deepcopy(head)
        answer = list()
        idx = 0
        while head:
            head = head.next
            idx += 1
        for i in range(math.floor(idx/2)):
            h = h.next
        return h
