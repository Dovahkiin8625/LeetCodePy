#
# @lc app=leetcode id=96 lang=python3
#
# [96] Unique Binary Search Trees
#

# @lc code=start
class Solution:
    def numTrees(self, n: int) -> int:
        r_ = [1]+[0]*n
        for i in range(1,n+1):
            for j in range(i):
                r_[i] += r_[j]*r_[i-1-j]
        return r_[n]
# @lc code=end

