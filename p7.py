# https://www.geeksforgeeks.org/google-interview-experience-off-campus/
stream = raw_input()
stream = [int(x) for x in stream.split()]
w_k_stream = raw_input()
w,k =int(w_k_stream.split()[0]),int(w_k_stream.split()[1])

if w < 2*k:
    print(0)
    exit()

import heapq
min_k_heap = []
max_w_k_heap = []

max_k_heap = []
min_w_k_heap = []

sum = 0
count = 0

def deleteFromMaxHeap(heap, element):
    # The value of the elements in the maxHeap are stored in the negative index
    idx = heap.index(-element)
    heap[idx] = heap[-1]
    heap.pop()
    heapq.heapify(heap)

def deleteFromMinHeap(heap, element):
    idx = heap.index(element)
    heap[idx] = heap[-1]
    heap.pop()
    heapq.heapify(heap)

# def insertIntoM
def isNumberInSum(number):




# really good problem to solve, and I am kind of struck in it
w_array = []

def deleteTheElement(element):
    if i < -max_k_heap[0]:
        deleteFromMaxHeap(element)

for i in stream:
    if -max_k_heap[0] < i and i < min_k_heap[0]:
        sum  = sum + i - get()
        count = getCount()
        print sum/count
