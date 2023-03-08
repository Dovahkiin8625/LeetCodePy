'''
Given head, the head of a linked list, determine if the linked list has a cycle in it.
There is a cycle in a linked list if there is some node in the list that 
can be reached again by continuously following the next pointer. 
Internally, pos is used to denote the index of the node that tail's next pointer is connected to. 
Note that pos is not passed as a parameter.
Return true if there is a cycle in the linked list. Otherwise, return false.

给定的头，链表的头，确定链表是否有循环。
如果列表中存在某个节点，可以通过连续跟踪下一个指针再次到达，则链表中存在一个循环。
在内部，pos 用于表示 tail 的下一个指针连接到的节点的索引。请注意，pos 不会作为参数传递。
如果链表中存在循环，则返回 true。否则，返回 false。
'''
from typing import Optional, Callable, Any, Tuple
import json

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 解决方法
# 遍历链表，将每个节点放入字典中， 每个节点检查是否已在字典里
class DictSolution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        p = head
        s = {}
        while p.next:
            if p in s:
                return True
            s.add(p)
        return False

            

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
            
            # ret = Solution().reverseList(head)
            out = DictSolution().hasCycle(head)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()