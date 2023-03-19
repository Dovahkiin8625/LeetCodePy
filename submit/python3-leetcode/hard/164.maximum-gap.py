#
# @lc app=leetcode id=164 lang=python3
#
# [164] Maximum Gap
#
from typing import List
# @lc code=start
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        len_ = len(nums)
        if len_ < 2: return 0
        if len_ == 2: return abs(nums[0]-nums[1])
        max_,min_ = max(nums),min(nums)
        max_gap = 0
        bucket_len = max(1,(max_-min_)//(len_ - 1))
        buckets = [[] for _ in range( (max_-min_)//bucket_len+1) ]

        for n in nums:
            loc = (n - min_)//bucket_len
            buckets[loc].append(n)
        # print(buckets)
        
        pre_max = max(buckets[0])
        for b in range(1,len(buckets)):
            if buckets[b] :
                max_gap = max(max_gap,min(buckets[b])-pre_max)
                pre_max = max(buckets[b])
        return max_gap
        
    
# if __name__ == "__main__":
#     nums = [1,24,12,1,21,5]
#     a = Solution().maximumGap(nums)
#     print(nums,a)
                
# @lc code=end

