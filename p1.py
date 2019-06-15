# https://www.geeksforgeeks.org/google-interview-experience-off-campus/

votes = {}
mappingOfIdxToId = {}
mappingOfIdToIdx = {}
# at zero position we will be storing the idx in the heap
# and at second position we will be storing the count of votes
idx = 0
def voteCandidate(id):
    if id in votes:
        votes[id] = 1 + votes[id]
        hp[ mappingOfIdToIdx[id]  ] = votes[id]
        heapifyUp(mappingOfIdToIdx[id])
    else:
        votes[id] = 1
        mappingOfIdToIdx = id
        hp[idx] = 1
        mappingOfIdxToId[idx] = id
        idx = idx + 1

    # heapify()
    # There can be some paths that can be created on the heaps etc that can be used later on

# Assuming the heap is already there
hp = [None] * 100
def heapifyUp(idx):
    if idx == 0:
        return
    if hp[idx//2] > hp[idx]:
        mappingOfIdxToId[idx], mappingOfIdToIdx[idx//2] = mappingOfIdxToId[idx//2], mappingOfIdToIdx[idx]
        mappingOfIdToIdx[ mappingOfIdxToId[idx] ], mappingOfIdToIdx[ mappingOfIdxToId[idx//2] ] = mappingOfIdToIdx[ mappingOfIdxToId[idx//2] ], mappingOfIdToIdx[ mappingOfIdxToId[idx] ]
        hp[idx], hp[idx//2]  = hp[idx//2], hp[idx]
        heapifyUp(idx//2)

def heapifyDown(n, idx):
     largest = idx
     l = 2*idx + 1
     r = l + 1
     if l < n and hp[l] > hp[largest]:
         largest = l
     if r < n and hp[r] > hp[largest]:
         largest = r
     if idx != largest:
        mappingOfIdxToId[idx], mappingOfIdToIdx[largest] = mappingOfIdxToId[largest], mappingOfIdToIdx[idx]
        mappingOfIdToIdx[ mappingOfIdxToId[idx] ], mappingOfIdToIdx[ mappingOfIdxToId[largest] ] = mappingOfIdToIdx[ mappingOfIdxToId[largest] ], mappingOfIdToIdx[ mappingOfIdxToId[idx] ]
        hp[idx], hp[largest]  = hp[largest], hp[idx]
        heapifyDown(largest)

def getTopK(k):
    top = []
    for i in range(0,k):
        top.append(mappingOfIdToIdx[0])
        hp[0],hp[n-1-i] = hp[n-i-1],hp[0]
        mappingOfIdxToId[0], mappingOfIdxToId[n-1-i] = mappingOfIdxToId[n-i-1], mappingOfIdxToId[0]
        mappingOfIdToIdx[0],mappingOfIdToIdx[n-1-i] = mappingOfIdToIdx[n-i-1], mappingOfIdToIdx[0]
        heapifyDown(n-i, 0)
    for i in top[::-1]:
        heapifyUp(mappingOfIdToIdx[i])
    return top

    # deleting elements from the heap
    #x

# Implement the min heap and max heap, This kind of questions will be asked to me
