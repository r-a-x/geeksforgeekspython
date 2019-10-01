# https://leetcode.com/problems/regular-expression-matching/submissions/
def isMatch(s, p):
    m = len(p) + 2
    n = len(s) + 2

    dp = [[False]*m for _ in range(n)]
    dp[0][0] = True

    n = len(s)
    m = len(p)

    for i in range(1, m+1):
        dp[0][i] = False
        if p[i-1] == '*':
            dp[0][i] = dp[0][i-2]
    # "aaa"
# "ab*a*c*a"
    for i in range(1, n+1):
        for j in range(1, m+1):
            if p[j-1] == '.' or (p[j-1] == s[i-1]):
                dp[i][j] = dp[i-1][j-1]
            elif p[j-1] == '*':
                dp[i][j] = dp[i][j-2]
                if p[j-2] == s[i-1] or (p[j-2] == '.'):
                    dp[i][j] = dp[i][j] or dp[i-1][j]

    for i  in range(n+1):
        print dp[i]
    return dp[n][m]

s="aaa"
p="ab*a*c*a"
print isMatch(s, p)
