#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#
from typing import List

# @lc code=start
class MySolution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i,l = 0,len(nums)
        while i < l:
            if nums[i]==0:
                for j in range(i,l-1):
                    nums[j],nums[j+1] =nums[j+1],nums[j]
                l -= 1
            else:
                i+=1
class BetterSolution:
    def moveZeroes(self, nums: List[int]) -> None:
        inser = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i],nums[inser] = nums[inser],nums[i]
                inser += 1
from ast import literal_eval
if __name__ == "__main__":
    while True:
        try:
            data_in = input().strip("nums = ")
            nums = literal_eval(data_in)
            BetterSolution().moveZeroes(nums)
            print(nums)
        except Exception as e:
            print(e)
            break


        
# @lc code=end

