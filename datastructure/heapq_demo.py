import heapq

nums = [1,8,12,2,0, -12, 88,-1]

print(heapq.nlargest(3, nums))
print(heapq.nsmallest(3, nums))
print(heapq.heapify(nums))
print(nums)