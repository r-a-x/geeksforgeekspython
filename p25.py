# https://www.geeksforgeeks.org/number-of-ways-to-reach-the-end-of-matrix-with-non-zero-and-value/
matrix = [
    [1, 2, 1],
    [1, 1, 0],
    [2, 1, 1]
]
n = len(matrix)
m = len(matrix[0])
dp = [[[0]*21 for _ in range(m)] for _ in range(n)]


def getArrayValue(i, j, matrix):
    if i < 0 or j < 0:
        return [0]*21;
    return matrix[i][j]

# so If that's
for i in range(n):
    for j in range(m):
        for k in range(1, 21):
            dp[i][j][ k & matrix[i][j] ] = getArrayValue(i-1, j, dp)[k] + getArrayValue(i, j-1, dp)[k]
ct = 0
for i in range(1, 21):
    ct = ct + dp[n-1][m-1][i]
print ct
