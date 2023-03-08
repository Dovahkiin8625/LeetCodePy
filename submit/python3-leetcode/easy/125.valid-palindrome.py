#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = "".join(filter(str.isalnum, s)).lower()
        i, j = 0, len(st)-1
        while i < j:
            if st[i] != st[j]: return False
            i += 1; j -= 1
        return True
# @lc code=end

