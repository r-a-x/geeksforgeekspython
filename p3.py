# https://www.geeksforgeeks.org/google-interview-experience-off-campus/
import heapq
l=[]
mp = {}
heapq.heapify(l)
def startReq(id, startTime):
    heapq.heappush(l,(startTime,id))
    pass

def finishReq(id, endTime):
    mp[id] = endTime
    pass


def printAll():
    sortedList = heapq.nlargest(len(list), l)
    # printing the sorted list over here
    # for i in sortedList:
        # print
