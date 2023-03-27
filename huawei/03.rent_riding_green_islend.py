'''
题目
[租车骑绿岛] 100分
部门组织绿岛骑行团建活动。租用公共双人自行车，每辆自行车最多坐两人，最大载重M。给出部门每个人的体重，请问最少需要租用多少双人自行车。
输入描述:
第一行两个数字m、n，分别代表自行车限重，部门总人数。第二行，n个数字，代表每个人的体重，体重都小于等于自行车限重m.
0<m<=200
0<n<=1000000
输出描述:
最小需要的双人自行车数量。
示例1 输入输出示例仅供调试，后台判题数据一般不包含示例
输入
34
3 2 2 1
输出
3
'''
import sys
m,n = (int(i) for i in input().strip().split())
ws = [int(i) for i in input().strip().split()]


ws.sort()
# 最重的人超重,返回0
if m<ws[-1]:
    print(0)
    sys.exit(0)

i,j,rst = 0,len(ws)-1,0 

while i <= j:
    if ws[i] +ws[j] <= m:
        i += 1
    j -= 1
    rst += 1
print(rst)


