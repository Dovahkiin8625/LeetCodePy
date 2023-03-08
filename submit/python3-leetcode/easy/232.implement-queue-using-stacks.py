#
# @lc app=leetcode id=232 lang=python3
#
# [232] Implement Queue using Stacks
#

# @lc code=start
class MyQueue:

    def __init__(self):
        self.in_ = []
        self.out_ = []

    def push(self, x: int) -> None:
        self.in_.append(x)

    def pop(self) -> int:
        self.peek()
        return self.out_.pop()

    def peek(self) -> int:
        if not self.out_:
            while self.in_:
                self.out_.append(self.in_.pop())
        return self.out_[-1]

    def empty(self) -> bool:
        return not self.in_ and not self.out_
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @lc code=end

