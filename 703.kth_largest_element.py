from typing import List
import heapq
class SortKthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        if k>0:
            nums.sort(reverse=True)
            self.kth:list=nums[:k]
    def add(self, val: int) -> int:
        if len(self.kth)<self.k:
            self.kth.append(val)
        elif val>=self.kth[-1]:
            self.kth[-1]=val
        self.kth.sort(reverse=True)
        return self.kth[-1]
    
class HeapKthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        if k>0:
            nums.sort(reverse=True)
            self.kth:list=nums[:k]
    def add(self, val: int) -> int:
        if len(self.kth)<self.k:
            self.kth.append(val)
        elif val>=self.kth[-1]:
            self.kth[-1]=val
        self.kth.sort(reverse=True)
        return self.kth[-1]

if __name__=='__main__':
    kl = SortKthLargest(3,[])
    print(kl.add(12))
    print(kl.add(121))
    print(kl.add(1))
    print(kl.add(123))

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)