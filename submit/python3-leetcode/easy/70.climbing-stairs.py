#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
from typing import List
class Solution:
    def climbStairs(self, n: int) -> int:
        dp:List[int] = [0]*(n+1)
        dp[0:3] = [0,1,2]
        for i in range(3,n+1):
            dp[i]=dp[i-1] + dp[i-2]
        return dp[n]
        
# @lc code=end

# if __name__ == '__main__':
