 # https://www.geeksforgeeks.org/rearrange-numbers-in-an-array-such-that-no-two-adjacent-numbers-are-same/
try:
    import Queue as Q
except ImportError:
    import queue as Q

ar = [1,2,3,1,]
q = Q.PriorityQueue()
ct = {}
for i in ar:
    if i not in ct:
        ct[i] = 0
    ct[i] = ct[i] + 1

print ct
for value,count in ct.items():
    q.put((-count,count,value))

sol = []

while not q.empty():
    cmp,count,value = q.get()
    if count <= 0:
        continue
    sol.append(value)

    if not q.empty():
        next_cmp,next_count,next_value = q.get()
        sol.append(next_value)
    else:
        print "No solution to the problem, Go to hell!!!"
        break
    q.put((-count+1, count-1,value))
    q.put((-next_count+1, next_count-1,next_value))
print sol
