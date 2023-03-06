# from collections import queue
from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        mapper = {'(':')','[':']','{':'}'}
        for c in s:
            if c in mapper:
                stack.append(c)
            elif not stack or mapper[stack.pop()] !=c :
                return False
        return not stack
    
if __name__ == '__main__':
    str_ = '('
    print(Solution().isValid(str_))