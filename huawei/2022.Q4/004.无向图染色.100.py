'''
[无向图染色] 100
----------------------------------------------------------------
给一个无向图只染色，可以填红黑两种颜色，
必须保证相邻两个节点不能同时为红色，输出有多少种不同的染色方案?
----------------------------------------------------------------
输入描述:
第一行输入M(图中节点数) N(边数)
后续N行格式为: V1 V2表示一个V1到V2的边。
数据范围: 1 <= M <= 15.0 = N <= M3，不能保证所有节点都是连通的.
输出描述:
输出一个数字表示染色方案的个数。
----------------------------------------------------------------
示例1:
输入:
4 4
1 2
2 4
3 4
1 3
输出:
7
说明:4个节点，4条边，1号节点和2号节点相连，2号节点和4号节点相连，
3号节点和4号节点相连，1号节点和3号节点相连，
若想必须保证相邻两个节点不能同时为红色，总共7种方案。
'''
import functools
#处理输入
input_param = [int(x) for x in input().split(" ")]
m = input_param[0]
n = input_param[1]
 
#构造边的数据结构
edges = []
for i in range(n):
    edges.append([int(x) for x in input().split(" ")])
print(edges)
 
count = 0
for i in range((1 << m)):
    flag = True;
    for j in range(n):
        print(i,j)
        #检测所有的边相连的是否同为红颜色
        if ((i >> (m-edges[j][0]) & 1) == 1 and (i >> (m-edges[j][1]) & 1)==1):
            flag = False
            break

    if flag:
        print(i)
        count += 1 
print (count)