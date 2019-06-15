# https://www.geeksforgeeks.org/google-interview-experience-off-campus/

n=4
M=[]
K=[]
# When I connect source and destination, there might be an issue with something
par = [None]*n

def getParent(id):
    if par[id] == None:
        return id
    parent = getParent(par[id])
    par[id] = parent
    return parent



def addEdge(source, destination):
    sourceParent = getParent(source)
    destinationParent = getParent(destination)
    for vertex in K:
        if getParent(vertex[0]) == sourceParent or getParent(vertex[0]) == destinationParent:
            if getParent(vertex[1]) == sourceParent or getParent(vertex[1]) == destinationParent:
                return
    par[sourceParent] = destinationParent
