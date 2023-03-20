#
# @lc app=leetcode id=590 lang=python3
#
# [590] N-ary Tree Postorder Traversal
#

# @lc code=start

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

from typing import List
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        def porder(root: 'Node',out_:List[int])->List[int]:
            if root is None:
                return 
            for c in root.children:
                porder(c, out_)
            out_.append(root.val)
        out_:List[int] = []
        porder(root, out_)
        return out_

# @lc code=end

