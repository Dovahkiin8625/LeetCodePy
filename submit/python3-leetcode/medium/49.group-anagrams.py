#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#
from typing import List
# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
            使用哈希表
            1. 将每个字符串排序，作为key
            2. 将每个字符串检查key是否在字典中存在，如果存在将该字符串插入到value列表，
        '''
        st:dict = {}
        for s in strs:
            a = list(s)
            a.sort()
            a = ''.join(a)
            st[a] = st.get(a,[])
            st[a].append(s)
            
        return [st[i] for i in st.keys()]        
# @lc code=end
# from ast import literal_eval
# if __name__ == '__main__':
#     while True:
#         try:
#             inputs = input().strip('strs = ')
#             strs = literal_eval(inputs)
#             print(Solution().groupAnagrams(strs))
#         except Exception as e:
#             print(e)
#             break
