#
# @lc app=leetcode id=438 lang=python3
#
# [438] Find All Anagrams in a String
#
from collections import List
# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        '''
            使用字典，用p中每个字符的数量进行初始化。
            初始化一个滑动窗口，统计窗口中个字符的数量，将字符作为key，数量作为value。
            窗口滑动过程中，移出窗口的字符在字典中维护该key的数量+1，新增字符数量-1，
            判断字典中是否所有value 为0，如果为0 说明p的每个字符数量与s该窗口的字串每个字符数量相等，则返回
        '''
        diff,index = {},[]
        for p_ in p:
            diff[p_] = diff.get(p_, 0) + 1
        for i in range(len(s)):
            if i >= len(p):
                diff[s[i-len(p)]] += 1
            diff[s[i]] = diff.get(s [i], 0) - 1
            if all(x ==0 for x in diff.values()):
                index.append(i-len(p)+1)
        return index
# @lc code=end

