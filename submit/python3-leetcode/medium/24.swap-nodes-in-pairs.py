#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional, Callable, Any, Tuple
import json
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        xh = ListNode(0)
        p,p.next = xh,head
        while p.next and p.next.next:
            a = p.next
            b = a.next
            p.next,a.next,b.next =  b,b.next,a
            p = a
        return xh.next
# @lc code=end

