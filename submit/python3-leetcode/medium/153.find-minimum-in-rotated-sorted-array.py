#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#
from typing import List
# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        # if len(nums) == 1: return nums[0]
        l_,h_ = 0,len(nums)-1
        while l_ < h_:
            mid = (l_+h_)//2
            if nums[mid] < nums[h_]:
                h_ = mid
            else:
                l_ = mid+1
            
        return nums[l_]
    
if __name__ == '__main__':
    print(Solution().findMin([2,1]))
# @lc code=end

