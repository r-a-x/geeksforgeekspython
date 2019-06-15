# https://www.geeksforgeeks.org/kth-largest-element-in-a-stream/
# Finding the kth largest element in the stream of numbers

def getKthLargestFromTheInfiniteStreamOFNumbers(number):
    if number < heap[0]:
        return heap[0]
    if len(heap) == k:
        heapq.heappop(heap)
        heapq.heappush(heap, number)
    if len(heap) < k:
        heapq.heappush(heap, number)
    return heap[0]

import heapq
l=[]
# This will be a min heap, so the top element will represent the kth largest element
heapq.heapify(l)
