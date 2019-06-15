# https://www.geeksforgeeks.org/find-triplets-array-whose-sum-equal-zero/
stream = raw_input().split()
arr = [int(x) for x in stream]


def findTriplet(arr):
    found = False
    for i in range(len(arr)):
