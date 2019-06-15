#https://www.geeksforgeeks.org/google-interview-experience-off-campus/
# The problem is to figure out the array from the various sub arrays
from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(lambda:[])

    def addEdge(self, u, v):
        self.graph[u].append(v)
        # Adding an  edge one side to the component
        # The working of the stack is such that it will be going somewhere and used from that place

    def dfs(self, u, stack, visited):
        if visited[u]:
            return
        visited[u] = True
        for v in self.graph[u]:
            if not visited[v]:
                self.dfs(v, stack, visited)
        stack.append(u)


    def topologicalSort(self):
        visited = [False]*self.V
        stack = []
        visited = defaultdict(lambda:False)
        for i in range(0, self.V):
            self.dfs(i, stack, visited)
        return stack[::-1]

g = Graph(5)
g.addEdge(0,2)
g.addEdge(2,1)
g.addEdge(2,3)
g.addEdge(3,4)
g.addEdge(1,3)

print g.topologicalSort()
