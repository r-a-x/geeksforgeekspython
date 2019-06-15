# https://www.geeksforgeeks.org/generate-all-binary-strings-from-given-pattern/
def printStr(str, index):
    if index == len(str):
        print(str)
        return
    if str[index] == '?':
        for ch in ['0','1']:
            str[index] = ch
            printStr(str, index + 1)
            str[index] = '?'
    else:
        printStr(str, index + 1)

str = raw_input().split()
printStr(str, 0)
