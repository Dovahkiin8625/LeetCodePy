#
# @lc app=leetcode id=127 lang=python3
#
# [127] w Ladder
#
from typing import List
# @lc code=start
from collections import defaultdict,deque
class Solution:
    def ladderLength(self, bw_: str, ew_: str, ws: List[str]) -> int:
        if not bw_ or not ew_ or not ws or ew_ not in ws: return 0
        if bw_ == ew_: return 1

        len_ = len(bw_)
        diag = defaultdict(list)
        for w in ws:
            for i in range(len_):
                diag[w[:i]+'_'+w[i+1:]].append(w)
        # print(diag)
        set_ = {bw_}
        q_ = deque([(bw_,1)])
        while q_:
            w, l = q_.popleft()
            for i in range(len_):
                subs_ = diag[w[:i]+'_'+w[i+1:]]
                for s in subs_:
                    if s == ew_:
                        return l+1
                    if s not in set_:
                        set_.add(s)
                        q_.append((s,l+1))
            # print(q_)
        return 0

# @lc code=end

