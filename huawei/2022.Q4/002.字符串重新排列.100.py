'''
[字符串排序] 100
----------------------------------------------------------------
给定一个字符串s,s包括以空格分隔的若干个单词,请对s进行如下处理后输出:
1、单词内部调整: 对每个单词字母重新按字典序排序
2、单词间顺序调整:
1) 统计每个单词出现的次数，并按次数 降序排列
2) 次数相同，按单词长度 升序排列
3) 次数和单词长度均相同，按字典升序排列
请输出处理后的字符串，每个单词以一个空格分隔。
----------------------------------------------------------------
输入描述:
行字符串，每个字符取值范围: [a-ZA-Z0-9] 以及空格，字符串长度范围: [1,1000]
----------------------------------------------------------------
例1:
输入
This is an apple
输出
an is This aelpp
例2:
输入:
My sister is in the house not in the yard
输出:
in in eht eht My is not adry ehosu eirsst
'''

from functools import cmp_to_key
from collections import defaultdict

words = input().strip().split()

for i in range(len(words)):
    words[i] = "".join(sorted(words[i]))
# print(words)
# a,b : (str:count)  1: a排在b后
def cmp(a,b):
    if a[1]<b[1]:
        return 1
    elif a[1]>b[1]:
        return -1
    else:
        if len(a[0])>len(b[0]):
            return 1
        elif len(a[0])<len(b[0]):
            return -1
        else:
            if a[0]>b[0]:
                return 1
            elif a[0]<b[0]:
                return -1
            else:
                return 0
            
words_count = defaultdict(int)
for w in words:
    words_count[w] += 1

words_sort = sorted(words_count.items(), key=cmp_to_key(cmp))
print(words_sort)
rst = ""
for s,n in words_sort:
    for i in range(n):
        rst += s + " "
print(rst)
# rst = 


            
