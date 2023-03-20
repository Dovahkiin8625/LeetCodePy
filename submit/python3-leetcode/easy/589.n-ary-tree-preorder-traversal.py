#
# @lc app=leetcode id=589 lang=python3
#
# [589] N-ary Tree Preorder Traversal
#

# @lc code=start
from typing import List
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


# class Solution:
#     def preorder(self, root: 'Node') -> List[int]:
#         def porder(root: 'Node',out_: List[int]) -> List[int]:
#             if root is None: return
#             out_.append(root.val)
#             for c  in root.children:
#                 porder(c, out_)
                
#         out_ = []
#         porder(root,out_)
#         return out_
class Solution:
    def preorder(self,root: 'Node')-> List[int]:
        if root is None:
            return []
        out_ = []
        stack = [root]
        while stack:
            node = stack.pop()
            print(node.val)
            out_.append(node.val)
            for i in range(1,len(node.children)+1):
                if node.children[-i] is not None:
                    stack.append(node.children[-i])
        return out_


# @lc code=end

