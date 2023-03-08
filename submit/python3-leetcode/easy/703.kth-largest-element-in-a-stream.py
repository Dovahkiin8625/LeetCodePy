#
# @lc app=leetcode id=703 lang=python3
#
# [703] Kth Largest Element in a Stream
#

# @lc code=start
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        if k>0:
            nums.sort(reverse=True)
            self.kth:list=nums[:k]
    def add(self, val: int) -> int:
        if len(self.kth)<self.k:
            self.kth.append(val)
        elif val>=self.kth[-1]:
            self.kth[-1]=val
        self.kth.sort(reverse=True)
        return self.kth[-1]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
# @lc code=end

