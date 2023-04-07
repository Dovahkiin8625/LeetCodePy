#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#
from typing import List
# @lc code=start
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         dict = {}
#         for i in range(len(nums)):
#             if (target - nums[i]) in dict:
#                 return dict[target- nums[i]],i
#             dict[nums[i]] = i
#         return 0,0
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = nums.copy()
        nums.sort()
        l,r = 0,len(nums)-1
        while l < r:
            tmp = nums[l]+nums[r]
            if tmp< target:
                l+=1
            elif tmp>target:
                r-=1
            else:
                break
        return [i for i in range(len(nums)) if nums[l]==a[i] or nums[r]==a[i]]
        

# @lc code=end

