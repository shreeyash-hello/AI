from collections import defaultdict

class graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addedge(self,u,v):
        self.graph[u].append(v)

    def dfsmain(self, v, visited):
        visited.add(v)
        print(v, end=" ")
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.dfsmain(neighbour,visited)

    def dfs(self,v):
        visited = set()
        self.dfsmain(v,visited)

obj = graph()
number_of_edges = int(input("enter number of edges: "))
for i in range (number_of_edges):
    u = int(input("enter node"))
    neigh = int(input("enter number of neighbours: "))
    for n in range(neigh):
        v = int(input("enter neighbour"))
        obj.addedge(u,v)


start = int(input("enter starting node: "))

print("dfs of the graph is: ")
obj.dfs(start)