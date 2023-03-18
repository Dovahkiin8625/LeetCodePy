#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#
from typing import List

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(n):
            j = m-1
            while j >= 0 and nums1[j]>nums2[i]:
                nums1[j+1] = nums1[j]
                j-=1
            nums1[j+1]= nums2[i]
            m+=1
            # print(nums1)
        
# if __name__=="__main__":
#     nums1,nums2= [2,0],[1]
#     Solution().merge(nums1,1,nums2,1)
#     print(nums1)

        
# @lc code=end

