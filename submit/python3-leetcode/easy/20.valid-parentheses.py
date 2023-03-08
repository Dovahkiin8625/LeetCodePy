#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#
from collections import deque

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        mapper = {'(':')','[':']','{':'}'}
        for c in s:
            if c in mapper:
                stack.append(c)
            elif not stack or mapper[stack.pop()] !=c :
                return False
        return not stack
        
# @lc code=end

