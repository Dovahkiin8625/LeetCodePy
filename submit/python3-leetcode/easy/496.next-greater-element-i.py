#
# @lc app=leetcode id=496 lang=python3
#
# [496] Next Greater Element I
#
from typing import List
# @lc code=start
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict_,stack = {},[]

        for n in reversed(nums2):
            while stack and n >= stack[-1]:
                stack.pop()
            dict_[n] = stack[-1] if stack else -1
            stack.append(n)

        return [dict_[i] for i in nums1]
# if __name__ == "__main__":
#     print(Solution().nextGreaterElement([4,1,2],[1,3,4,2]))
        
# @lc code=end

