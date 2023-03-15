from typing import List, Callable
import random
from time import perf_counter

# 冒泡排序
def bubble_sort(nums: List[int]):
    for i in range(len(nums)):
        for j in range(len(nums)-i-1):
            if nums[j] >= nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]

# 直接选择排序 每次取最大(小)
def select_sort(nums: List[int]):
    for i in range(len(nums)):
        min = i
        for j in range(i, len(nums)):
            if nums[j] < nums[min]:
                min = j
        nums[i], nums[min] = nums[min], nums[i]

# 插入排序, 插入有序列表
def insert_sort(nums: List[int]):
    for i in range(1, len(nums)):
        tmp = nums[i]
        j = i-1
        while j >= 0 and tmp < nums[j]:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = tmp

# 希尔排序, 插入排序的优化版,不同于插入排序, 希尔排序将插入排序分为多个组,每个组使用插入排序
# 使整个序列趋于基本有序
def shell_sort(nums: List[int]):
    n = len(nums)
    # 生成增量
    h = 0
    while h < n:
        h = 3*h + 1
    while h >= 1:
        for i in range(h, n):
            tmp = nums[i]
            j = i-h
            while j>=0 and tmp < nums[j]:
                nums[j+h] = nums[j]
                j -= h
            nums[j+h] = tmp
        h = (h-1)//3

# 快速排序
def quick_sort(nums: List[int]):
    def partition(nums: List[int], left: int, right: int):
        pivot = nums[right]
        tail = left
        for i in range(left, right):
            if nums[i] < pivot:
                nums[i], nums[tail] = nums[tail], nums[i]
                tail += 1
        nums[right], nums[tail] = nums[tail], nums[right]
        return tail

    def sort(nums: List[int], left: int, right: int):
        if left >= right:
            return
        pivot = partition(nums, left, right)
        sort(nums, left, pivot-1)
        sort(nums, pivot+1, right)
    sort(nums, 0, len(nums)-1)

# 使用python特性(迭代器)快速排序
def quick_sort_py(nums: List[int]):
    def sort(nums: List[int]):
        if len(nums) < 2:
            return nums
        pivot = nums[0]
        left = [i for i in nums[1:] if i < pivot]
        right = [i for i in nums[1:] if i >= pivot]
        return sort(left) + [pivot] + sort(right)
    sorted_nums = sort(nums)
    for i in range(len(nums)):
        nums[i] = sorted_nums[i]

# 一行实现快排
def quick_sort_inline(nums: List[int]):
    def sort(array): return array if len(array) <= 1 else sort(
        [item for item in array[1:] if item <= array[0]]) + [array[0]] + sort([item for item in array[1:] if item > array[0]])
    sorted_nums = sort(nums)
    for i in range(len(nums)):
        nums[i] = sorted_nums[i]

def merge_sort(nums: List[int]):
    def merge(left:List[int],right:List[int]):
        l,r = 0, 0
        m = []
        while l<len(left) and r<len(right):
            if left[l] < right[r]:
                m.append(left[l])
                l+=1
            else:
                m.append(right[r])
                r+=1
        m += left[l:]
        m += right[r:]
        return m
    def sort(nums: List[int]):
        if len(nums)<=1: return nums
        mid = len(nums)//2
        left = sort(nums[:mid])
        right = sort(nums[mid:])
        return merge(left,right)
    sorted_nums = sort(nums)
    for i in range(len(sorted_nums)):
        nums[i] = sorted_nums[i]


if __name__ == "__main__":
    def test_sort_method(nums: List[int], type: str, sort: Callable):
        print(f"{type:}--------")
        n = nums.copy()
        f = perf_counter()
        print(f"Before sorting: {n}")
        sort(n)
        print(f"After sorting: {n}")
        print(f"Time spent:{perf_counter()-f}\n")
        pass

    # test_nums = random.randint(0, 999)
    test_nums = [random.randint(0, 999) for i in range(10)]
    test_sort_method(test_nums, 'Bubble sort', bubble_sort)
    test_sort_method(test_nums, 'Select sort', select_sort)

    test_sort_method(test_nums, 'Insert sort', insert_sort)
    test_sort_method(test_nums, 'Shell sort', shell_sort)

    test_sort_method(test_nums, 'Quick sort', quick_sort)
    test_sort_method(test_nums, 'Quick sort py', quick_sort_py)
    test_sort_method(test_nums, 'Quick sort inline', quick_sort_inline)

    test_sort_method(test_nums, 'Merge sort', merge_sort)