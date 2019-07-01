# https://www.geeksforgeeks.org/construct-bst-from-given-preorder-traversa/
# o(n) Implementation
# It contains the O(n) implementation of creating a binary search tree from preorder traversal
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

# There
def constructUtil(pre, idx, mn, mx):
    print(idx, mn, mx)
    if idx < 0 or len(pre) <= idx:
        return None, idx

    i = idx + 1
    root = Node(pre[idx])
    if len(pre) <= idx + 1:
        return root, idx +1

    if mn <= pre[idx+1] and pre[idx+1] < root.data:
        root.left, idx = constructUtil(pre, idx+1, mn, root.data)
    else:
        idx = idx +1

    if len(pre) <= idx:
        return root, idx

    if root.data <= pre[idx] and pre[idx] < mx:
        root.right, idx = constructUtil(pre, idx, root.data, mx)

    return root, max(i, idx)


def constructTree(pre):
    return constructUtil(pre, 0, float('-Inf'), float('Inf'))

# pre = [10, 5, 1, 7, 40, 50]
pre = [90,80,70,60,50,40,30,20,10]
root = constructTree(pre)
printInorderTree(root[0])
# constructing the tree in o(n) is also possible
