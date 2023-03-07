
'''
Given two strings s and p, return an array of all the start indices of p's anagrams in s. 
You may return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
给定两个字符串 s 和 p，返回一个数组，其中包含 p 在 s 中的字谜的所有起始索引。 您可以按任何顺序返回答案。
Anagram 是通过重新排列不同单词或短语的字母而形成的单词或短语，通常只使用所有原始字母一次。
'''

from typing import List
class SolutionDict:
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
class SolutionTwoDict:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        '''
  使用两个字典，一个记录p的字母数量，另一个用于记录滑动窗口字母数量，两个字典相等，则添加到输出
        '''
        pd,sd,index  = {},{},[]
        for p_ in p:
            pd[p_] = pd.get(p_, 0) + 1
        for i in range(len(s)):
            if i >= len(p):
                sd[s[i-len(p)]] -= 1
                if sd[s[i-len(p)]] <=0:
                    sd.pop(s[i-len(p)])

            sd[s[i]] = sd.get(s[i],0)+1
            if pd == sd:
                index.append(i-len(p)+1)
        return index

import collections
class SolutionCounter:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        '''
        方法类似，区别是，使用两个Counter， 一个是p的数量，一个是窗口的字符数量

        '''
        cp=collections.Counter(p)
        sp=collections.Counter(s[:len(p)])
        output=[]
        i=0
        j=len(p)
        # 从窗口尾循环
        while j<=len(s):
            if sp==cp:
                output.append(i)
            # 数量相等 添加到输出

            sp[s[i]]-=1 # 去除窗口首项计数
            if sp[s[i]]<=0:
                sp.pop(s[i]) # 数量为0 时 pop出去
                
            if j<len(s):    
                 sp[s[j]]+=1
            j+=1
            i+=1
            
        return output

if __name__ == '__main__':
    while True:
        try:
            data = input().strip().split(',')
            s = data[0][5:-1]
            p = data[1][6:-1]
            print(SolutionTwoDict().findAnagrams(s, p))
        except Exception as e:
            break
