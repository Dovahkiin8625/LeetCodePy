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
def graph_dyeing1():
    # 遍历所有节点的情况, 使用二进制表示节点的颜色,1为红色
    # 例如总共4个节点则有2^4(1<<4)种情况,分别为 0000,0001,0010,0011...1111 
    # 所以,判断n节点的颜色只需要将二进制数右移n-1位后和0001做与操作即可:
    #   比如0100,判断第3个节点颜色,将0100>>2 = 0001,0001&0001=1为红,
    #   判断第4个节点颜色,将0100>3=0000,0000&0001 = 0, 为黑
    #   (此处也可以将0001左移n-1位,)
    #注意:此处是从右往左表示每个节点,比如0001表示1节点红,其他黑, 如果从左往右表示,
    #则需要将二进制数i右移 m-n位, 结果一致.
    m_,n_ = map(int,input().strip().split())
    edges = []
    for i in range(n_):
        edges.append([int(i) for i in input().strip().split()])

    rst = 0
    for i in range(1<<m_):
        flag = True
        for edge in edges:
            # 判断边的
            if i>>(edge[0]-1)&1 == 1 and i>>(edge[1]-1)&1 == 1:
                flag = False    
                break
        if flag:
            rst+=1
    print(rst)

def graph_dyeing2():
    m_,n_ = map(int,input().strip().split())
    edges = []
    for i in range(n_):
        edges.append([int(i) for i in input().strip().split()])
    rst=0
    for i in range(1<<m_):
        flag = True
        for edge in edges:
            # 两条边节点先转为二进制表示,再和i与运算, 如果结果等于bedge,即相邻为红
            bedge = (1<<(edge[0]-1))+(1<<(edge[1]-1))
            if bedge==bedge&i:
                flag = False    
                break
        if flag:
            rst+=1
    print(rst)

def graph_dyeing3():
    m_,n_ = map(int,input().strip().split())
    edges = []
    for i in range(n_):
        edges.append(input().strip().split())

    all_nodes = "".join([str(i+1) for i in range(m_)])
    err_count = 0
    al = []
    for x in range(len(all_nodes)):
        for i in range(len(all_nodes)-x):
            sub_str = all_nodes[i:i+x+1]
            al.append(sub_str)

            # for edge in edges:
            #     if edge[0] in sub_str and edge[1] in sub_str:
            #         err_count+=1
            #         break
    print(al)
    # print((1<<m_)-err_count)

graph_dyeing3()


    # err_set = {}
