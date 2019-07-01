# https://www.geeksforgeeks.org/paper-cut-minimum-number-squares-set-2/
def solve(n, m):
    dp = [[0]*(m+2) for _ in range(n+2)]
    for i in range(1, n+1):
        for j in range(i, m+1):
            if i == j:
                dp[i][j] = 1
                continue
            dp[i][j] = float("Inf")
            for x in range(0, i):
                for y in range(0, j):
                    dp[i][j] = min(dp[i][j], dp[min(x, y)][max(x, y)] + dp[min(i-x, y)][max(i-x, y)] + dp[min(i, j-y)][max(i, j-y)])
                    dp[i][j] = min(dp[i][j], dp[min(x, y)][max(x, y)] + dp[min(i-x, j)][max(i-x, j)] + dp[min(x, j-y)][max(i, j-y)])
    print dp[n][m]

n = 30
m = 36
print solve(min(n, m), max(n, m))
