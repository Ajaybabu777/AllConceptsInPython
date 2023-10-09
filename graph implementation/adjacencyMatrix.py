# undirected and unweighted graph
class Graph:
    def __init__(self, noOfNodes):
        self.noOfNodes = noOfNodes
        self.AdjMatrix = []
        for i in range(noOfNodes):
            row = [0]*noOfNodes
            self.AdjMatrix.append(row)

    def addEdge(self, val1, val2):
        self.AdjMatrix[val1][val2] = 1
        self.AdjMatrix[val2][val1] = 1

    def display(self):
        rows = self.AdjMatrix
        for row in rows:
            print(row)

g = Graph(4)
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(0,3)
g.addEdge(1,3)
g.addEdge(1,2)
g.addEdge(2,3)

g.display()

