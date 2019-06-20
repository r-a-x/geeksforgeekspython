#https://www.geeksforgeeks.org/how-to-print-maximum-number-of-a-using-given-four-keys/
def printA(n):
    if n < 7:
        return n
    dp = [0]*(n+1)
    for i in range(1,7):
        dp[i] = i
    for i in range(7, n+1):
        for j in range(i-3, 1, -1):
            dp[i] = max(dp[i], dp[j]*(i-j-1))
    return dp[n]

n = 12
print printA(n)
