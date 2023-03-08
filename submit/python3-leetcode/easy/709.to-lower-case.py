#
# @lc app=leetcode id=709 lang=python3
#
# [709] To Lower Case
#

# @lc code=start
class Solution:
    def toLowerCase(self, s: str) -> str:
        return ''.join(chr(ord(c)|32) if 65<=ord(c) <=90 else c for c in s )
# @lc code=end

