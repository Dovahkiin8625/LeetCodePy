'''
[真正密码] 100
在一行中输入一个字符串数组，如果其中一个字符串的所有以索0开头的子串在数组中都有，那么这个字符串就是潜在密码，
在所有潜在密码中最长的是真正的密码，如果有多个长度相同的真正的密码，那么取字典序最大的为唯一的真正的密码，求唯一的真正的密码。
示例1:
输>: h he hel hell hello o ok n ni nin ninj ninjaa
输出: ninja
说明:按要求，helo、ok、ninia都是潜在密码。检查长度，helo、ninia是真下的密码、检查字曲序，ninia是唯一真正密码
示例2:
输入:
a b c d f
输出: 
f
说明: 按要求，abcdf都是潜在密码。检查长度，a b c d f是真正的密码。检查字典序，f 是唯一真正密码
'''

# import sys
passwds = input().strip().split()
rst = ''
for p in passwds:
  # 如果下标为0的所有子串都在字典中 all([p[:j] in passwds for j in range(1,len(p))])
  # 且 长度大于当前所选真实密码, 或者长度相等,但是字典序大于当前真实密码
  if all([p[:j] in passwds for j in range(1,len(p))]) and (len(p)>len(rst) or (len(p)==len(rst) and p>rst)):
    rst = p
print(rst)
    