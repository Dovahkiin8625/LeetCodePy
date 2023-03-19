#
# @lc app=leetcode id=179 lang=python3
#
# [179] Largest Number
#
from typing import List
# @lc code=start
class Solution:
    # 选择排序
    def largestNumber(self, nums: List[int]) -> str:
        for i in range(len(nums)):
            mj = i
            for j in range(i,len(nums)):
                if self.compare(nums[j],nums[mj]):
                    mj = j
            nums[mj],nums[i] = nums[i],nums[mj]
        return str(int("".join(map(str,nums))))
    def compare(self, n1,n2):
        return str(n1)+str(n2)>str(n2)+str(n1)
# @lc code=end

