'''
----------------------------------------------------------------
输入一个长度为4的倍数的字符串，字符串中仅包含WASD四个字母。
将这个字符串中的连续子串用同等长度的仅包含WASD的字符串替换，
如果替换后整个字符串中WASD四个字母出现的频数相同，那么我们称替换后的字符串是“完美走位”。
求子串的最小长度。
如果输入字符串已经平衡则输出0。
----------------------------------------------------------------
[输入]
一行字符表示给定的字符串s
数据范围：
1<=n<=10^5且n是4的倍数，字符串中仅包含WASD四个字母。
[输出]
一个整数表示答案
----------------------------------------------------------------
[样例输入输出]
示例1：
输入：
WASDAASD
输出：
1
说明：
将第二个A替换为W，即可得到完美走位 。
示例2：
输入：
AAAA
输出：
3
说明：
将其中三个连续的A替换为WSD，即可得到完美走位  
'''
from collections import defaultdict
in_ = input().strip()
steps = defaultdict(int)
for i in in_:
    steps[i] += 1
# avg_s = sum(steps.values())//4
max_s = max(steps,key= lambda x: steps[x])
diff = max(steps.values())-sum(steps.values())//4
print(steps,max_s,diff)

if diff == 0:
    print(0)
i,j = 0, diff
# while j

# print(steps)
# print(sum(steps.values()))
