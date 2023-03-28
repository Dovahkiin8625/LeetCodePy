'''
[最大利润] 100
商人经营一家店铺，有number 种商品，
由于仓库限制每件商品的最大持有数量是 item[index]
每种商品的价格是 item-price[item_index][day]
通过对商品的买进和卖出获取利润
请给出商人在 days 天内能获取的最大的利润
注:同一件商品可以反复买进和卖出
输入描述
3 第一行输入商品的数量 number
3 第二行输入商品售货天数 days
4 56第二行输入仓库限制每件商品的最大持有数量是itemindex]
123第一件商品每天的价格
4 32第二件商品每天的价格
153 第三件商品每天的价格
输出描述:
商人在 days 天内能获取的最大的利润
示例1:
输入:
3
3
4 5 6
1 2 3
4 3 2
1 5 3
输出:
32
示例2:
输入:
1
输出:
0
'''
n_ = int(input().strip())
d_ = int(input().strip())
it_ =[int(i) for i in input().strip().split()]
itp_ = []
for i in range(n_):
    itp_.append([int(j) for j in input().strip().split()])
    
rst = 0
for i in range(n_):
    m_ = 0
    for j in range(d_-1):
        m_ += max(0,itp_[i][j+1]-itp_[i][j])
    rst += m_*it_[i]
print(rst)
