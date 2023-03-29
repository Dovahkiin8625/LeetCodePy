'''
[单向链表中间节点] 100
----------------------------------------------------------------
题目描述
求单向链表中间的节点值，如果奇数个节点取中间，偶数个取偏右边的那个值。
----------------------------------------------------------------
输入描述：
第一行 链表头节点地址path 后续输入的节点数n
后续输入每行表示一个节点，格式:   "节点地址  节点值  下一个节点地址(-1表示空指针)“
输入保证链表不会出现环，并且可能存在一些节点不属于链表。
输出描述：
链表中间节点值。
----------------------------------------------------------------
测试用例:
输入:
00010 4
00000 3 -1
00010 5 12309
11451 6 00000
12309 7 11451
输出:
6
'''
# [构造链表方法]
def middle_node1():
    class Node:
        def __init__(self, val:int=0,next=None):
            self.val = val
            self.next = next

    head,n_ = input().strip().split()
    n_ = int(n_)
    n_map = {} #addr:Node
    # 1. 根据每行输入构造字典n_map = {addr:Node},此时Node的next属性存放下一个节点的地址
    for i in range(n_):
        n_addr,n_val,n_next = input().strip().split()
        n_map[n_addr] = Node(n_val,n_next)
    # 2. 遍历字典将每个Node的next设置为实际的下一个节点Node本身
    for n in n_map:
        n_map[n].next = n_map[n_map[n].next] if n_map[n].next != '-1' else None
    # 3. 设置头,循环遍历n/2次,找到中间节点
    head = n_map[head]
    size_div2 = n_//2+1 if n_%2 else n_//2 # 如果奇数个节点取中间，偶数个取偏右边的那个值
    for i in range(size_div2):
        head = head.next
    print(head.val)
    # while node != None:
    #     print(node.val)
    #     node = node.next
# [字典查找方法]
def middle_node2():
    head,n_ = input().strip().split()
    n_ = int(n_)
    n_map = {} #addr:node
    # 1. 获取输入构造字典,value不是Node 而是dict = {'val': n_val, 'next': n_next}
    for i in range(n_):
        n_addr,n_val,n_next = input().strip().split()
        n_map[n_addr] = {
            'val':n_val,
            'next':n_next
        }
    # 2. 遍历字典,循环n/2次, 找到中间节点
    size_div2 = n_//2+1 if n_%2 else n_//2
    now = n_map[head]
    for i in range(size_div2):
        now = n_map[now['next']]
    print(now['val'])
    
middle_node2()
