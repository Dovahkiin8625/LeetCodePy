from collections import defaultdict
def solution(nums):
  map_ = defaultdict(int)
  count = 0
  for n in nums:
    if map_[-n]==n:
      count+=1
    map_[n] = -n
  return count
print(solution([2,1, -1,-2, 3]))