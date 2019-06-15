# https://www.geeksforgeeks.org/construct-bst-from-given-preorder-traversa/
class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

def printInorderTree(root):
    if root is None:
        return
    printInorderTree(root.left)
    print(root.data)
    printInorderTree(root.right)

def constructUtil(pre, low, high):
    print (low, high)
    if low > high or high >= len(pre):
        return None

    root = Node(pre[low])

    if low == high:
        return root

#   remember to handle the edge case if there is no node
    par = high+1

    for i in range(low, high+1):
        if pre[i] > pre[low]:
            par = i
            break

    root.left = constructUtil(pre, low+1, par-1)
    root.right = constructUtil(pre, par, high)
    return root


def constructTree(pre):
    return constructUtil(pre, 0, len(pre)-1)

# pre = [10, 5, 1, 7, 40, 50]
pre = [90,80,70,60,50,40,30,20,10]
root = constructTree(pre)
printInorderTree(root)
# constructing the tree in o(n) is also possible
#
