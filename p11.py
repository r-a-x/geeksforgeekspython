#https://www.geeksforgeeks.org/find-subarray-with-given-sum/
def findTheSum(arr, sum):
    start = 0
    cur_sum = arr[0]
    if cur_sum == sum:
        print("Found the sum in the array",0)
        return
    for i in range(1, len(arr)):
        while sum < cur_sum and start < i:
            cur_sum -= arr[start]
            start += 1
        if cur_sum == sum:
            print("Found the sum in the array",start,i-1)
            return
        if cur_sum < sum:
            cur_sum += arr[i]

arr = raw_input().split()
arr = [int(x) for x in arr]
sum = int(raw_input())
findTheSum(arr, sum)
