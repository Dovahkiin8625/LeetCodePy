#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional,List
class Solution:
    # def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    #     return self.inorderTraversal(root.left)+[root.val]+self.inorderTraversal(root.right) if root else []
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        r_,s_ = [],[root]
        while s_:
            n_ = s_.pop()
            if isinstance(n_,TreeNode):
                s_.extend([n_.right,n_.val,n_.left])
            elif isinstance(n_,int):
                r_.append(n_)
            
        return r_

# @lc code=end

