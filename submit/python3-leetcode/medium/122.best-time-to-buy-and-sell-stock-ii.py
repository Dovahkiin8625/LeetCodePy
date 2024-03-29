#
# @lc app=leetcode id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        rst = 0
        for i in range(len(prices)-1):
            if prices[i+1]>prices[i]:
                rst+= prices[i+1]-prices[i]
        return rst
    
# @lc code=end

