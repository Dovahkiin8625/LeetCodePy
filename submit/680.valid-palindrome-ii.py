#
# @lc app=leetcode id=680 lang=python3
#
# [680] Valid Palindrome II
#

# @lc code=start
class Solution:
    def validPalindrome(self, s: str) -> bool:
        i,j,hf = 0,len(s)-1,int(len(s)/2)
        while i < j:
            if s[i] != s[j] :
                si,sj = s[i:hf],s[-hf:j]
                return si[]
            i+=1;j-=1
        return True

# @lc code=end

