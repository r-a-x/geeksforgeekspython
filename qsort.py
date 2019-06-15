
def qsort(list, low, high):
    print (list,low,high)
    if low >= high:
        return

    p = partition(list, low, high)
    qsort(list, low, p-1)
    qsort(list, p+1, high)

# I have reference to something that is useful that can be done
# Let's see what can be done from my end
def partition(list, low, high):
    # print(list, low, high)
    k = high-1
    # It stores the smallest element known till now.
    lindex = low - 1
    for i in range(low, high-1):
        if list[i] <= list[k]:
            list[lindex+1],list[i] = list[i], list[lindex+1]
            lindex = lindex + 1
    list[lindex+1], list[k] = list[k], list[lindex+1]
    return lindex+1

list  = [12,300,23,230]
qsort(list, 0, len(list))
print (list)
