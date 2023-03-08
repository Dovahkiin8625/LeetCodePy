#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#
from collections import List
# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        f,b,max_a = 0,len(height)-1,(len(height)-1)*min(height[0],height[len(height)-1])
        while f<b:
            if height[f]>height[b]:
                temp = height[b]*(b-f)
                b-=1
            else:
                temp = height[f]*(b-f)
                f+=1
            max_a = max(max_a,temp)                  
        return max_a
            
# @lc code=end

