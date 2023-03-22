#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        r = [True]
        for i in range(1, len(s)+1):
            r+= any(r[j] and s[j:i] in wordDict for j in range(i)),
        return r[-1]
# @lc code=end

