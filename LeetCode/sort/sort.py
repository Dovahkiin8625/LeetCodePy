from typing import List,Callable
import random
from time import process_time_ns,time_ns,perf_counter
# 冒泡排序
def bubble_sort(nums: List[int]):
    for i in range(len(nums)):
        for j in range(len(nums)-i-1):
            if nums[j] >= nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]

def quick_sort(nums:List[int]):
    def partition(nums: List[int],left:int,right:int):
            pivot = nums[right]
            tail = left
            for i in range(left,right):
                if nums[i] < pivot:
                    nums[i],nums[tail] =nums[tail],nums[i]
                    tail+=1
            nums[right],nums[tail] = nums[tail],nums[right]
            return tail
    def sort(nums:List[int],left:int,right:int):
        if left >= right:
            return
        pivot = partition(nums,left,right)
        sort(nums,left,pivot-1)
        sort(nums,pivot+1,right)
    sort(nums,0,len(nums)-1)
        


if __name__ == "__main__":
    def test_sort_method(nums: List[int],type:str, sort:Callable):
        print(f"{type:}--------")
        n = nums.copy()
        f = perf_counter()
        print(f"Before sorting: {n}")
        sort(n)
        print(f"After sorting: {n}")
        print(f"Time spent:{perf_counter()-f}")
        pass

    # test_nums = random.randint(0, 999)
    test_nums = [random.randint(0,999) for i in range(10)]
    test_sort_method(test_nums,'Bubble sort',bubble_sort)
    test_sort_method(test_nums,'Quick sort',quick_sort)
    # print(t2-t1)

