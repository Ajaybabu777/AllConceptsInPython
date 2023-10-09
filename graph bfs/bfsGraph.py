from collections import deque

def bfsGraph(start, graph):
    visited = set()
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            print(node)
            queue.extend(graph[node] - visited)

graph = {}
noOfEdges = int(input("please eneter number of edges \n"))

for i in range(noOfEdges):
    print("enter values of val1 and val2: \n")
    val1, val2 = input().split()
    

    if val1 not in graph:
        graph[val1] = set()
    if val2 not in graph:
        graph[val2] = set()

    graph[val1].add(val2)
    graph[val2].add(val1)

print("starting point")
print()
start = input()


bfsGraph(start, graph)