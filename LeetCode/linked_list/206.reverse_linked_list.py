'''
反转链表
给定单向链表的头部，反转列表，并返回反转列表。
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
'''
from typing import Optional, Callable, Any, Tuple
import json

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 解决方法
# 1. 将p 作为链表的前节点
# 2. 处理单个c时，需要，将c.next = p 
#   并再下次循环时 将p = c， c= c.next 即下次循环时， 前序节点为当前节点，当前节点为下一个节点
# 3. 所以得到语句 c.next = p, p = c, c = c.next 即 c.next,p,c = p,c,c.next
# 4. 循环完成后，p即最后一个节点
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        c,p = head,None
        while c:
            c.next,p,c = p,c,c.next
        return p
            

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
            
            ret = Solution().reverseList(head)

            out = listNodeToString(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()