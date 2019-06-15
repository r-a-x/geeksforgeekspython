# https://www.geeksforgeeks.org/find-triplets-array-whose-sum-equal-zero/
ar = raw_input().split()
ar = [ int(x) for x in ar ]
print ar
sum = int(raw_input())
print sum
from collections import defaultdict
isExist = defaultdict(lambda:(False,None))

for i in range(len(ar)):
    # Assuming all the numbers are unique in the arrays
    # If there are duplicates it won't work
    isExist[sum-ar[i]] = (True,i)

print isExist
for i in range(len(ar)):
    print ar[i]
    print isExist[sum - ar[i]]
    if isExist[ar[i]][0]:
        if isExist[ar[i]][1] != i:
            print "Yes it exists"
            print ar[i], ar[isExist[ar[i]][1]]
