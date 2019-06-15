# https://www.geeksforgeeks.org/check-binary-tree-contains-duplicate-subtrees-size-2/
def constructUtil(pre, low, high):
    # print (low, high)
    if low > high or high >= len(pre):
        return None

    root = Node(pre[low])

    if low == high:
        return root

#   remember to handle the edge case if there is no node
    par = high+1

    for i in range(low, high+1):
        if pre[i][0] > pre[low][0]:
            par = i
            break

    root.left = constructUtil(pre, low+1, par-1)
    root.right = constructUtil(pre, par, high)
    return root


def constructTree(pre):
    return constructUtil(pre, 0, len(pre)-1)



class Node:
    def __init__(self, data):
        self.data = data
        self.right = self.left = None

MARKER = '$'
hash = {}

def duplicate(root):

    if root == None:
        return MARKER

    lstr = duplicate(root.left)
    if lstr == "":
        return ""

    rstr = duplicate(root.right)
    if rstr == "":
        return ""

    st = root.data[1] + lstr + rstr

    if len(st) > 3 and st in hash:
        return ""

    print(st)
    hash[st] = True
    return st

# I am using the preorder matrix to generate tree

#
pre = [(20,'a'), (10, 'c'), (5, 'd'), (15, 'e'), (30, 'c'), (25, 'd'), (40, 'e')]
root = constructTree(pre)

if duplicate(root) == "":
    print("Duplicate exists")
else:
    print("No duplicates")
