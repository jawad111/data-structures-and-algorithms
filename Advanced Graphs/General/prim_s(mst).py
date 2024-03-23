import heapq
# Given a list of edges of a connected undirected graph,
# with nodes numbered from 1 to n,
# return a list edges making up the minimum spanning tree.
def minimumSpanningTree(edges):
    
    adj = {}

    for src, dst, w in edges:
        adj[src] = []
        adj[dst] = []


    for src, dst, w in edges:
        adj[src].append([w, dst])


    mst = []
    visited = set()
    visited.add('A')

    heap_values = []
    for w, neighbour in adj['A']: # Pushing all neighbors of start node.
        heapq.heappush(heap_values, [w, 'A', neighbour])


    #while len(visited) < len(adj): # length of edges in mst must be smaller that total nodes (to avoid cycle)
    while len(heap_values) != 0:
        w, n1, n2 = heapq.heappop(heap_values)

        if n2 not in visited:
            mst.append([n1, n2])
            visited.add(n2)
            for w, neighbour in adj[n2]:
                if neighbour not in visited:
                    heapq.heappush(heap_values, [w, n2, neighbour])

    return mst

edges = [['A','B', 10],
         ['A','C', 3],
         ['B','D', 2],
         ['C','B', 4],
         ['C','D', 8],
         ['C','E', 2],
         ['D','E', 5],
         ]

print(minimumSpanningTree(edges))
        