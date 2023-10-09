def graphDfsPreorder(graph, node, visitedPlaces):
    
    if node not in visitedPlaces:
        print(node, end=",")
        visitedPlaces.add(node)

        for i in graph[node]:
            graphDfsPreorder(graph, i, visitedPlaces)

def graphDfsPostorder(graph, node, visitedPlaces):
    
    if node not in visitedPlaces:
        # print(node, end=",")
        visitedPlaces.add(node)

        for i in graph[node]:
            graphDfsPreorder(graph, i, visitedPlaces)
        print(node, end=",")

graph = {
    "A":["C","B"],
    "B":["A","D","E"],
    "C":["A"],
    "D":["B"],
    "E":["B","F"],
    "F":["E"]
}
node = "F"
visitedPlaces = set()
# graphDfsPreorder(graph, node, visitedPlaces)
graphDfsPostorder(graph, node, visitedPlaces)
