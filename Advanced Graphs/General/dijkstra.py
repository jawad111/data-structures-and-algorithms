import heapq
# Given a connected graph represented by a list of edges, where
# edge[0] = src, edge[1] = dst, and edge[2] = weight,
# find the shortest path from src to every other node in the
# graph. There are n nodes in the graph.
# O(E * logV), O(E * logE) is also correct.


def dijkstra(edges, src):
   
    adjacencyList = {}

    for connection in edges:
       adjacencyList[connection[0]] = [] # add src node
       adjacencyList[connection[1]] = [] # add dst node to make sure all node types are added


   
    # s = src, d = dst, w = weight
    for s, d, w in edges: # {'A': [], 'B': [], 'C': [], 'D': [], 'E': []}
       adjacencyList[s].append([w, d]) 


    shortest = {}
    heapValues = [[0, src]]

    while len(heapValues) != 0:
        w1, n1 = heapq.heappop(heapValues)

        if n1 not in shortest:
            
            shortest[n1] = w1

            for w2, n2 in adjacencyList[n1]: #{'A': [[10, 'B'], [3, 'C']], 'B': [[2, 'D']], 'C': [[4, 'B'], [8, 'D'], [2, 'E']], 'D': [[5, 'E']], 'E': []}
                if n2 not in shortest:
                    heapq.heappush(heapValues, [w1 + w2, n2])

    return shortest



edges = [['A','B', 10],
         ['A','C', 3],
         ['B','D', 2],
         ['C','B', 4],
         ['C','D', 8],
         ['C','E', 2],
         ['D','E', 5],
         ]

print(dijkstra(edges, 'A'))
        