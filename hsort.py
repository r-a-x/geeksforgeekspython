# Implementing
# n is the size of the list
def heapify(list, n, index):
    l = 2*index + 1
    r = 2*index + 2
    largest = index
    if l < n and list[l] > list[largest]:
        largest = l
    if r < n and list[r] > list[largest]:
        largest = r
    if largest != index:
        list[index],list[largest] = list[largest], list[index]
        heapify(list, n, largest)

def hsort(list):
    n = len(list)
    # Take the largest element from the
    # lets make a h
    # create a max heap out of the array let's see what can be done for that use case
    # heapify is working properly. Lets fix something else
    for i in range(n-1, -1, -1):
        heapify(list, n, i)
        # print (list)


    for i in range(n-1,-1,-1):
        list[i], list[0] =  list[0], list[i]
        heapify(list, i, 0);

# list = [0,-1,34,54,1,2,3,4,9,8,7]
list = [5, 6, 12, 13, 14, 0, -1, 123]
hsort(list)
print(list)
