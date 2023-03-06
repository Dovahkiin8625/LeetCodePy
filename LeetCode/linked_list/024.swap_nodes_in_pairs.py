"""
两两交换元素位置
给定一个链表，每两个相邻节点交换一次并返回其头部。
您必须在不修改列表节点中的值的情况下解决问题（即，只能更改节点本身）
Input: head = [1,2,3,4]
Output: [2,1,4,3]
"""
from typing import Optional, Callable, Any, Tuple
import json

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 解决方法[]
# 1. 生成链表的head前节点xh ， p 作为head前节点，要交换的两个节点分别为a、b
# 2. p.next = b , a.next = b.next , b.next = a
# 3. 交换完成后 需要将p 移到下一个需要交换的节点前， 即交换后的 a
# 4. 交换后的链表头节点即 xh.next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        xh = ListNode(0)
        p,p.next = xh,head
        while p.next and p.next.next:
            a = p.next
            b = a.next
            p.next,a.next,b.next =  b,b.next,a
            p = a
        return xh.next


            

def stringToIntegerList(input):
    return json.loads(input)

def stringToListNode(input):
    # Generate list from the input
    numbers = stringToIntegerList(input)

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr

def listNodeToString(node):
    if not node:
        return "[]"

    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"

def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            head = stringToListNode(line);
            
            ret = Solution().swapPairs(head)

            out = listNodeToString(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()