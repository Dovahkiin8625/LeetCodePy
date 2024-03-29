# 两数之和
# 题目: 整数数组和一个目标值,请再改数组中找出和为目标值的

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         dict = {}
#         for i in range(len(nums)):
#             if (target - nums[i]) in dict:
#                 return dict[target- nums[i]],i
#             dict[nums[i]] = i
#         return 0,0
from typing import List
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
        
if __name__=='__main__':
    nums = [ int(i) for i in input().strip().split()]
    target = int(input().strip())
    i,j = Solution().twoSum(nums,target)
    print(i,j)