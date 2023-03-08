#
# @lc app=leetcode id=680 lang=python3
#
# [680] Valid Palindrome II
#

# @lc code=start
class Solution:
    def validPalindrome(self, s: str) -> bool:
        return self.palindrome(s, False)

    def palindrome(self, s: str, is_deleted: bool) -> bool:
        i, j = 0, len(s)-1
        while i < j:
            if s[i] != s[j]:
                if is_deleted:
                    return False
                return self.palindrome(s[i+1:j+1], True) or self.palindrome(s[i:j], True)
            i += 1
            j -= 1
        return True
# @lc code=end
