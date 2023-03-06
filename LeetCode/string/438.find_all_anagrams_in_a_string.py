
'''
'''

from typing import List
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
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

import collections
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        dict_p=collections.Counter(p)
        dict_s=collections.Counter(s[:len(p)])
        output=[]
        i=0
        j=len(p)
        
        while j<=len(s):
            if dict_s==dict_p:
                output.append(i)

            dict_s[s[i]]-=1
            if dict_s[s[i]]<=0:
                dict_s.pop(s[i])
                
            if j<len(s):    
                 dict_s[s[j]]+=1
            j+=1
            i+=1
            
        return output

if __name__ == '__main__':
    while True:
        try:
            data = input().strip().split(',')
            s = data[0][5:-1]
            p = data[1][6:-1]
            print(Solution().findAnagrams(s, p))
        except Exception as e:
            break
