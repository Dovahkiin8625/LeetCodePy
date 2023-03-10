from typing import List
import random
from time import process_time_ns,time_ns
# 冒泡排序
def bubule_sort(nums: List[int]):
    for i in range(len(nums)):
        for j in range(len(nums)-i-1):
            if nums[j] >= nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]



if __name__ == "__main__":
    # test_nums = random.randint(0, 999)
    test_nums = [random.randint(0,999) for i in range(53)]
    p1 = process_time_ns()
    t1 = time_ns()
    bubule_sort(test_nums)
    p2 = process_time_ns()
    t2 = time_ns()
    print(t1,t2,p1,p2)
