#!/usr/bin/env python3
# coding=utf-8

import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0
    
    # 这里的优先级判断是根据后面插入的元组的第一元素判断排序的
    def push(self, item, priority):
        heapq.heappush(self._queue, (priority, self._index, item))
        self._index += 1
    
    def pop(self):
        return heapq.heappop(self._queue)[-1]


p = PriorityQueue()

p.push("张三", 2)
p.push("李四", 1)
p.push("王五", -1)
p.push("赵六", 6)

print(p.pop())
print(p.pop())
print(p.pop())
print(p.pop())

