class Solution:
    def longestValidParentheses(self, s: str) -> int:
        l = len(s) + 1
        sum = [[float("-Inf")]*l for _ in range(l)]
        mn = [[float("Inf")]*l for _ in range(l)]

        sum[0][0] = mn[0][0] = 0
        l = len(s)

        for i in range(1, l+1):
            mn[0][i] = sum[0][i] = 0
            if s[i-1] == '(':
                mn[1][i] = sum[1][i] = 1
            else:
                mn[1][i] = sum[1][i] = -1

        ans = 0
        for i in range(2, l+1):
            for j in range(1, l+1):
                if s[j-1] == '(':
                    sum[i][j] = 1 + sum[i-1][min(l,j+1)]
                    mn[i][j] = 1 + mn[i-1][min(l,j+1)]
                else:
                    sum[i][j] = -1 + sum[i-1][min(l,j+1)]
                    mn[i][j] = -1 + mn[i-1][min(l,j+1)]
                ans = ans + 
        return ans
