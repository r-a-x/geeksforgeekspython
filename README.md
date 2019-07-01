These are the python solution of the google problems in the geeks for geeks
Python cheat sheet
5.0//2 = 2
length of the list len(ar)

smallest number  = float('-Inf')
largest number = float('Inf')

Ternary Operator
c = a if true else d
if the above condition is True
c = a
else
c = d

Arrays
c = [None]\*5
d = [[None]\*5]\*5

For using list as queue
the functions are
q = []
q.append()
q.pop(0)

by default pop() removes the last element


For sorting the list use the function
l = [ (k1, v1), (k2, v2), (k3, v3) ]
l.sort()
sorting will be done based on the keys k1,k2.. etc

for initializing the 2d array
dp = [[None]\*8 for _ in range(n)]
using solution like [[None]\*n]\*m leads to same reference [None]\*n being available to all the m repititions

Topics to work on
Heap

There is a Priority Queue in python
try:
    import Queue as Q
except ImportError:
    import queue as Q
pq = Q.PriorityQueue()

q.put()
q.get()
whiile not q.empty():
  pass


Heaps
import heapq
li = []
heapq.heapify(li)
heapq.heappush(li,4)
heapq.heappop(li)
