# directed and weighted graph

class Graph:
    def __init__(self, noOfNodes):
        self.noOfNodes = noOfNodes
        self.AdjMatrix = []
        for i in range(noOfNodes):
            row = [0]*noOfNodes
            self.AdjMatrix.append(row)

    def addEdge(self, val1, val2, weight):
        self.AdjMatrix[val1][val2] = weight
        # self.AdjMatrix[val2][val1] = weight

    def display(self):
        rows = self.AdjMatrix
        for row in rows:
            print(row)

g = Graph(4)
g.addEdge(0,1,4)
g.addEdge(0,2,91)
g.addEdge(0,3,7)
g.addEdge(1,3,6)
g.addEdge(1,2,10)
g.addEdge(2,3,12)

g.display()

