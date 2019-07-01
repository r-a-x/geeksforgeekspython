# heap Example
l = [ (101,"hi"), (12, "yours"), (1, "truly"), (122, "check")  ]
import heapq
print l
heapq.heapify(l)
print l
print heapq.heappop(l)
