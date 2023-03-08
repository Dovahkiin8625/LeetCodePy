#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#
from collections import List

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        inser = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i],nums[inser] = nums[inser],nums[i]
                inser += 1
         

        
# @lc code=end

