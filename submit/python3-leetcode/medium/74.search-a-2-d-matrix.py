#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#
from typing import List
# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or target is None: return False
        m_,n_ = len(matrix[0]),len(matrix)
        l_,h_ = 0,m_*n_-1
        while l_ <= h_:
            mid = (l_+h_)//2

            num = matrix[mid//m_][mid%m_]
            print(mid//m_,mid%n_,num)
            if num == target:
                return True
            elif num < target:
                l_ = mid +1
            else:
                h_ = mid - 1
        return False
if __name__ == '__main__':
    Solution().searchMatrix([[1,3]],3)

# @lc code=end

