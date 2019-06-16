# https://www.geeksforgeeks.org/find-if-a-string-is-interleaved-of-two-other-strings-dp-33/

def checkDP(a, al, b, bl, c):
    if al < 0 or bl < 0:
        return False
    if al == 0 and bl == 0:
         dp[0][0] = True
         return True
    if al == 0 and b[bl] == c[bl + al]:
        return dp[0][bl-1]
    if bl == 0 and a[al] == c[bl + al]:
        return dp[al-1][0]
    if dp[al][bl] != None:
        return dp[al][bl]
    dp[al][bl] = False
    if c[al + bl] != a[al] and c[al + bl] == b[bl]:
        dp[al][bl] = checkDP(a, al, b, bl-1, c)
    if c[al + bl] != b[bl] and c[al + bl] == a[al]:
        dp[al][bl] = checkDP(a, al-1, b, bl, c)
    if c[al + bl] == a[al] or c[al + bl] == b[bl]:
        dp[al][bl] = checkDP(a, al-1, b, bl, c) or checkDP(a, al, b, bl-1, c)
    return dp[al][bl]

def isInterleaved(a, b, c):
    if len(c) != len(a) + len(b):
        return False
    al = len(a)
    bl = len(b)
    a = '$' + a
    b = '$' + b
    c = '$' + c
    return checkDP(a, al, b, bl, c)

def isInterleavedIterative(a, b, c):
    al, bl, cl = len(a), len(b), len(c)
    if al + bl != cl:
        return False
    # al,bl = al+1, bl+1
    dp  = [[False]*(bl+1)]*(al+1)
    for i in range(0, al+1):
        for j in range(0, bl+1):

            if i == 0 and j == 0:
                dp[0][0] = True
                continue

            if i == 0:
                if b[j-1] == c[j-1]:
                    dp[i][j] = dp[i][j-1]
                else:
                    continue

            if j == 0:
                if a[i-1] == c[i-1]:
                    dp[i][j] = dp[i-1][j]
                    continue

            if c[i+j-1]  == a[i-1]:
                dp[i][j] = dp[i-1][j]

            if c[i+j-1] == b[j-1]:
                dp[i][j] = dp[i][j-1]

            if c[i+j-1] == a[i-1] and c[i+j-1] == b[j-1]:
                dp[i][j] = dp[i-1][j] or dp[i][j-1]

    return dp[al][bl]

a = "XY"
b = "ADC"
c = "AXYDC"
# dp = [[None]*(len(b)+2)]*(len(a)+2)
# i and j means for that length
# dp[0][0] = True
print isInterleavedIterative(a, b, c)
# print dp
# Solving it in a iterative fashion
