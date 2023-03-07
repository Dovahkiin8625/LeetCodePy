#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = "".join(filter(str.isalnum, s)).lower()
        lh = int(len(st)/2)
        if lh == 0:
            return True
        f, b = st[:lh], st[-lh:]
        return f == ''.join(b[len(b)-i-1] for i in range(len(b)))


# @lc code=end

