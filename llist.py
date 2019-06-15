class Node(object):
    def __init__(self, data = None, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev
    def get_data(self):
        return self.data
    def get_next(self):
        return self.next
    def get_prev(self):
        return self.prev
    def set_next(self, next):
        self.next = next
        return next

def getHalf(head):
    # Interesting way to ger the reference of the pointers
    slow = head
    fast = head.get_next()

    while fast != None:
        fast = fast.get_next()
        if fast != None:
            slow = slow.get_next()
            fast = fast.get_next()

    mid = slow.get_next()
    slow.set_next(None)
    return head, mid

def mergeRecursive(sortedA, sortedB):
    if sortedA == None:
        return sortedB
    if sortedB == None:
        return sortedA
    head = None
    if sortedA.get_data() > sortedB.get_data():
        head = sortedB
        head.set_next(mergeRecursive(sortedA, sortedB.get_next()))
    else:

    return head

def merge(sortedA, sortedB):
    head = ptr = None
    while sortedA != None and sortedB != None:
        if sortedA.get_data() > sortedB.get_data():
            if head == None:
                head = sortedB
                ptr = head
            else:
                ptr = ptr.next(sortedB)
            sortedB = sortedB.get_next()
        else:
            if head == None:
                head = sortedA
                ptr = head
            else:
                ptr = ptr.next(sortedA)
            sortedA = sortedA.get_next()

    while sortedA != None:
        if head == None:
            head = sortedA
            ptr = head
        else:
            ptr = ptr.next(sortedA)
        sortedA = sortedA.get_next()

    while sortedB != None:
        if head == None:
            head = sortedB
            ptr = head
        else:
            ptr = ptr.next(sortedB)
        sortedB = sortedB.get_next()

    return head

def mergeSort(head):
    if head == None or head.get_next() == None:
        return head
    a,b = getHalf(head)
    # traverse(a)
    # print("The other half")
    # traverse(b)
    sortedA = mergeSort(a)
    sortedB = mergeSort(b)
    return merge(sortedA, sortedB)


def traverse(node):
    if node != None:
        print(node.get_data())
        traverse(node.get_next())


head = Node(14)
headNext = head.set_next(Node(2))
headNextNext = headNext.set_next(Node(30))
headNextNextNext = headNextNext.set_next(Node(104))
headNextNextNextNext = headNextNextNext.set_next(Node(5))
headNextNextNextNextNext = headNextNextNextNext.set_next(Node(23))

head = mergeSort(head)

traverse(head)
