
#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class recursiveSolution:
    def climbStairs(self, n: int) -> int:
        '''
        n太大时会报错超时。
        '''
        return self.climbStairs(n-1)+self.climbStairs(n-2) if n>2 else n
from typing import List
class dbSolution:
    def climbStairs(self, n: int) -> int:
        '''
        动态规划算法 爬上第n层的方法即 n-1层和n-2层的和
        dp[n] = dp[n-1]+dp[n-2] (n>2)
        '''
        dp:List[int] = [0]*(n+1)
        dp[0:3] = [0,1,2]
        for i in range(3,n+1):
            dp[i]=dp[i-1] + dp[i-2]
        return dp[n]
# @lc code=end

# if __name__ == '__main__':
