#
# @lc app=leetcode id=429 lang=python3
#
# [429] N-ary Tree Level Order Traversal
#

# @lc code=start

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
from typing import List

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        def lorder(root:'Node',level:int,out_):
            if root is None: return
            out_[level] = out_.get(level,[])
            out_[level].append(root.val)
            for c in root.children:
                lorder(c,level+1,out_)
        out_ = {}
        lorder(root,0,out_)
        return [out_[i] for i in out_.keys()]
# @lc code=end

