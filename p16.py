# https://www.geeksforgeeks.org/connect-nodes-at-same-level/
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

class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.next = None

def addNext(root):
    if root == None:
        return root
    q = []
    q.append(root)
    q.append(None)
    # print q
    while len(q) != 0:
        node = q.pop(0)
        # print node
        # import time
        # print q
        # time.sleep(1)
        if node == None:
            if len(q) == 0:
                break
            else:
                q.append(None)
                continue
#       There will never be a case when there is no node after a non None node
#       At this point, the length of queue will be atleast 1
        if len(q) < 1:
            print("The queue length is less than 1")
            break
        node.next = q[0]
        if node.left != None:
            # print "Left getting inserted"
            q.append(node.left)
        if node.right != None:
            # print "Right getting inserted"
            q.append(node.right)
    return root

def printNext(root):
    if root != None and root.next != None:
        print(root.next.data)
    else:
        print(None)

def printInorderTree(root):
    if root is None:
        return
    printInorderTree(root.left)
    print(root.data," and the next is ")
    printNext(root)
    printInorderTree(root.right)

# pre = [20]
pre = [(20,'a'), (10, 'c'), (5, 'd'), (15, 'e'), (30, 'c'), (25, 'd'), (40, 'e')]
root = constructTree(pre)
# print root.data, root.left, root.right, root.next

root = addNext(root)
printInorderTree(root)
