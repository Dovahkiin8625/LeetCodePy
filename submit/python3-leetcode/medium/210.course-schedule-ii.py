#
# @lc app=leetcode id=210 lang=python3
#
# [210] Course Schedule II
#
from collections import defaultdict
from typing import List
# @lc code=start
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        g_,r_,v_ = defaultdict(list),[],[0]*numCourses
        for p in prerequisites:
            g_[p[0]].append(p[1])
        
        def dfs(node):
            # print(g_,v_,r_)
            if v_[node] == -1:
                return False
            if v_[node] == 1:
                return True
            v_[node] = -1
            for g in g_[node]:
                if not dfs(g):
                    return False
            v_[node] = 1
            r_.append(node)
            return True
        for n in range(numCourses):
            if not dfs(n):
                return []
            
        return r_

    # Solution().findOrder(2,)      

# @lc code=end

