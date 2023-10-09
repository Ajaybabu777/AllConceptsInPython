class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self,data):
        newNode = Node(data)
        if not self.head:
            self.head = newNode
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = newNode

class Graph:
    def __init__(self):
        self.adjList = {}

    def addEdge(self, val1, val2):
        if val1 not in self.adjList:
            self.adjList[val1] = LinkedList()
        else:
            self.adjList[val1].append(val2)


        if val2 not in self.adjList:
            self.adjList[val2] = LinkedList()
        else:
            self.adjList[val2].append(val1)





g = Graph()
g.addEdge("0","1")
g.addEdge("0","5")
g.addEdge("0","4")
g.addEdge("0","3")
g.addEdge("0","2")
g.addEdge("1","0")
g.addEdge("1","2")
g.addEdge("2","0")
g.addEdge("2","1")
g.addEdge("2","3")
g.addEdge("3","0")
g.addEdge("3","2")
g.addEdge("3","4")
g.addEdge("4","0")
g.addEdge("4","3")
g.addEdge("4","5")
g.addEdge("5","0")
g.addEdge("5","4")


for key, value in g.adjList.items():
    print(key, end = "->")
    current = value.head
    while current:
        print(current.data)
        current = current.next
    print("None",end = "->")

