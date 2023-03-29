'''
----------------------------------------------------------------
数字0、1、2、3、4、5、6、7、8、9分别关联 a~z 26个英文字母。
0 关联 "a","b","c"
1 关联 "d","e","f"
2 关联 "g","h","i"
3 关联 "j","k","l"
4 关联 "m","n","o"
5 关联 "p","q","r"
6 关联 "s","t"
7 关联 "u","v"
8 关联 "w","x"
9 关联 "y","z"
例如7关联"u","v"，8关联"x","w"，输入一个字符串例如“78”，
和一个屏蔽字符串“ux”,那么“78”可以组成多个字符串例如：“ux”，“uw”，“vx”，“vw”，过滤这些完全包含屏蔽字符串的每一个字符的字符串，然后输出剩下的字符串。
----------------------------------------------------------------
示例：
输入：
78
ux
输出：
uw vx vw
说明：ux完全包含屏蔽字符串ux，因此剔除
'''
map_ = {
    '0': 'abc',
    '1': 'def',
    '2': 'ghi',
    '3': 'jkl',
    '4': 'mno',
    '5': 'opr',
    '6': 'st',
    '7': 'uv',
    '8': 'wx',
    '9': 'yz'
}
num_str = input().strip()
filter_str = input().strip()
rst = []
# 递归得到字符排列组合,
def comb(sn, strs, idx):
    if len(sn) ==  idx:
        rst.append(strs)
        return
    for c in map_[sn[idx]]:
        comb(sn, strs+c, idx+1)
comb(num_str,'',0)
# 使用字典查找是否完全包庇
f_set = set(filter_str)
for s in rst:
    s_set = set(s)
    if_in = True
    for f in f_set:
        if f not in s_set:
            if_in = False
    if if_in:
        rst.remove(s)
print(" ".join(rst))

