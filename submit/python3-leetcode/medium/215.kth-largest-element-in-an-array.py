#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#
from typing import List
import heapq
# @lc code=start


class Solution:
    # 自带排序
    # def findKthLargest(self, nums: List[int], k: int) -> int:
    # nums.sort()
    # return nums[-k]

    # 自带堆
    # def findKthLargest(self, nums: List[int], k: int) -> int:
    #     return heapq.nlargest(k, nums)[-1]

    # 快排
    # def findKthLargest(self, nums: List[int], k: int) -> int:
    #     def quick_sort(nums):
    #         if len(nums) < 2:
    #             return nums
    #         else:
    #             base_value = nums[0]     # 选择基准值
    #             less = [m for m in nums[1:] if m < base_value]     # 由所有小于基准值的元素组成的子数组(python独有的切片，生成器等特性)
    #             greater = [m for m in nums[1:] if m >= base_value]   # 由所有大于基准值的元素组成的子数组
    #         return quick_sort(less) + [base_value] + quick_sort(greater)
    #     return quick_sort(nums)[-k]
    
    # 冒泡
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            for j in range(len(nums)-i-1):
                if nums[j]<nums[j+1]:
                    nums[j],nums[j+1] = nums[j+1],nums[j]
        
        return 0
