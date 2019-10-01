
def arrI(i):
    mx = float("-Inf")
    for j in range(k):
        mx = max(input[j][i], mx)
    return mx

def solve(arr, k):
    sol = []
    q = []
    for i in range(len(arr)):
        # Handle the edge case for zero length
        while len(q) != 0 and arr[i] > q[0][0]:
            q.pop(0)
        q.insert(0,(arr[i],i))
        if i >= k-1:
            while len(q) != 0 and q[-1][1] < i-k+1:
                q.pop()
            sol.append(q[-1])
    return sol

arr = [-10, 3, 4, -5, 3 ,2, 120, -120, 123, 18]
k = 3

print solve(arr, k)

# 100, 120, 100
# arr = []
# arr = [1]
#     < 3 - 3 + 1
# arr = [-10, 3, 4, -5, 3 ,2, 120, -120, 123, 18]
# 2,
#    2 <= 2-3
# 2 - 3 + 1
#    -10, 3, 4, -5, 2, 120
#   -100, 2, 3, -6
#   -200, 1, 3, -7

# Consider
