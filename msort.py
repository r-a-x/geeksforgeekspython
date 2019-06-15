# class LinkedList:
#     next,
#     prev
# Merge Sort Implementation
def msort(list):
    if len(list)<=1:
        return
    mid = len(list)//2
    L = list[mid:]
    R = list[:mid]
    msort(L)
    msort(R)
    i = j = k = 0
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            list[k] = L[i]
            i = i + 1
        else:
            list[k] = R[j]
            j = j + 1
        k = k + 1
    while i < len(L):
        list[k] = L[i]
        k = k + 1
        i = i + 1
    while j < len(R):
        list[k] = R[j]
        k = k + 1
        j = j + 1

list = [1,2,23232,-2,32,90]
msort(list)
print (list)

# Implementing various other things that needs to be done for the binary sort
