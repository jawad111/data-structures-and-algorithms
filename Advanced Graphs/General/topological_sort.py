# Given a directed acyclical graph, return a valid

# topological ordering of the graph. 

def topologicalSort(edges):

    adj = {}

    for src, dst in edges:
        adj[src] = []
        adj[dst] = []
    
    for src, dst in edges:
        adj[src].append(dst)

    
    sorted = []
    visited = set()

    for edge in adj:
        dfs(edge, adj, sorted, visited)

    sorted.reverse()

    return sorted

def dfs(src, adj, sorted, visited):
    if src in visited:
        return
    
    visited.add(src)

    for neighbour in adj[src]:
        dfs(neighbour, adj, sorted, visited)
    
    sorted.append(src)





edges = [['A','B'],
         ['A','C'],
         ['B','D'],
         ['C','E'],
         ['D','F'],
         ['E','F'],
         ['G','H'],
         ]

print(topologicalSort(edges))