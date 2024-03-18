# GraphNode used for adjacency list
class GraphNode:
    def __init__(self, val):
        self. val = val
        self.neighbors = []


# Given directed edges, build an adjacency
edges = [["A","B"], ["B", "C"], ["B", "E"], ["C", "E"], ["E" , "D"]]
                                
adjacencyList = {}

for src, dst in edges:
    if src not in adjacencyList:
        adjacencyList[src] = []
    if dst not in adjacencyList:
        adjacencyList [dst] = []
        adjacencyList[src].append (dst)


print(adjacencyList)