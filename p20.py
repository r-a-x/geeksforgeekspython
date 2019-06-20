# https://www.geeksforgeeks.org/inplace-rotate-square-matrix-by-90-degrees/
def rotateMatrix(matrix):
    if not matrix:
        return
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if i < (n+1)/2 and j < (n+1)/2:
                matrix[i][j], matrix[n-j-1][i], matrix[n-i-1][n-j-1], matrix[j][n-i-1] = matrix[n-j-1][i] ,matrix[n-i-1][n-j-1], matrix[j][n-i-1], matrix[i][j]
                # i,j = n-j-1, i
                # n-j-1,i = n-i-1, n-j-1
                # n-i-1, n-j-1 = j, n-i-1
                # j, n-i-1 = i, j


matrix = [
    [1 ,2 ,3 ,4 ,5 ,6 ],
    [7 , 8, 9,10,11,12],
    [13,14,15,16,17,18],
    [19,20,21,22,23,24],
    [25,26,27,29,29,30],
    [31,32,33,34,35,36]
]

rotateMatrix(matrix)
for i in matrix:
    print i
