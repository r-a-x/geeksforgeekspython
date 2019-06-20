#https://www.geeksforgeeks.org/minimum-insertions-to-form-a-palindrome-dp-28/
# Minimum number of insertion to make a string palindrome
# Also the Pallindromic string obtained after doing this

str = "abcd"
l = len(str)
dp = [[None]*l for _ in range(l)]
pd = [[None]*l for _ in range(l)]
for i in range(0, l):
    dp[i][i] = 0
    pd[i][i] = str[i]
    if i + 1 < l:
        dp[i][i+1] = 0 if str[i] == str[i+1] else 1
        if str[i] == str[i+1]:
            pd[i][i+1] = str[i] + str[i+1]
        else:
            pd[i][i+1] = str[i] + str[i+1] + str[i]

for h in range(2, l):
    for i in range(0, l):
        if i + h < l:
            dp[i][i+h] = dp[i+1][i + h -1] if str[i] == str[i + h] else min(dp[i][i+h-1], dp[i+1][i+h]) + 1
            if str[i] == str[i+h]:
                pd[i][i+h] = str[i] + pd[i+1][i+h-1] + str[i+h]
            else:
                if dp[i][i+h-1] > dp[i+1][i+h]:
                    pd[i][i+h] = str[i] + pd[i+1][i+h]+ str[i]
                else:
                    pd[i][i+h] = str[i+h] + pd[i][i+h-1] + str[i+h]
 
print dp[0][l-1]
print pd[0][l-1]
