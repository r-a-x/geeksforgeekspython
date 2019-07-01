# https://www.geeksforgeeks.org/merge-two-bsts-with-limited-extra-space/
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
        if pre[i] > pre[low]:
            par = i
            break

    root.left = constructUtil(pre, low+1, par-1)
    root.right = constructUtil(pre, par, high)
    return root


def constructTree(pre):
    return constructUtil(pre, 0, len(pre)-1)

class Traverse:
    def __init__(self, root):
        self.root = root;
        self.st = [root]

    def getNext(self):
        while len(self.st) > 0:
            cur =  self.st.pop()
            if cur == None:
                continue
            if cur.left == None and cur.right == None:
                return cur
            if cur.left == None:
                self.st.append(cur.right)
                return cur
            if cur.right == None:
                left = cur.left
                cur.left = None
                self.st.append(cur)
                self.st.append(left)
            elif cur.left != None and cur.right != None:
                left = cur.left
                cur.left = None
                self.st.append(cur)
                # self.st.append(cur)
                # cur.right = None
                self.st.append(left)
        return None

class Node:
    def __init__(self, data):
        self.data = data
        self.left, self.right  = None,None

def mergeTwoBst(root1, root2):
    t1, t2 = Traverse(root1), Traverse(root2)
    n1, n2 = t1.getNext(), t2.getNext()

    while n1 != None and n2 != None:
        if n1.data > n2.data:
            print n2.data
            n2 = t2.getNext()
        else:
            print n1.data
            n1 = t1.getNext()

    while n1 != None:
        print n1.data
        n1 = t1.getNext()

    while n2 != None:
        print n2.data
        n2 = t2.getNext()


root1 = constructTree([20, 10, 15, 12, 18, 25, 30])
root2 = constructTree([10, 9, 8, 7, 6, 5, 4])
mergeTwoBst(root1, root2)
