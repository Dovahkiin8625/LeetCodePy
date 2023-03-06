'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
给定一个字符串数组 strs，将变位词组合在一起。 您可以按任何顺序返回答案。
Anagram 是通过重新排列不同单词或短语的字母而形成的单词或短语，通常只使用所有原始字母一次。
'''
from typing import List
from ast import literal_eval
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
if __name__ == '__main__':
    while True:
        try:
            inputs = input().strip('strs = ')
            strs = literal_eval(inputs)
            print(Solution().groupAnagrams(strs))
        except Exception as e:
            print(e)
            break
