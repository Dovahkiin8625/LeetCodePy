#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def sub_palindrome(s:str, l:int, r:int):
            sub_str: str = ''
            while l >= 0 and r <= len(s)-1 and s[l] == s[r]:
                sub_str = s[l:r+1]
                l-=1;r+=1
            return sub_str
        longest_p:str = ''
        for i in range(len(s)):
            sub_str:str = sub_palindrome(s,i,i)
            if len(sub_str) > len(longest_p): longest_p = sub_str
            sub_str:str = sub_palindrome(s,i,i+1)
            if len(sub_str) > len(longest_p): longest_p = sub_str
        return longest_p


# @lc code=end
