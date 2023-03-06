from collections import deque
class MyStack:

    def __init__(self):
        self.in_queue = deque()
        self.out_queue = deque()

    def push(self, x: int) -> None:
        self.in_queue.append(x)
        while self.out_queue:
            self.in_queue.append(self.out_queue.popleft())
        self.out_queue,self.in_queue = self.in_queue,self.out_queue

    def pop(self) -> int:
        return self.out_queue.popleft()
        
    def top(self) -> int:
        return self.out_queue[0]

    def empty(self) -> bool:
        return not self.out_queue
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()