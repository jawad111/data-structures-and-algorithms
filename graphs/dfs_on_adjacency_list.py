# Time: O(N^V)
# where N is number of choices each node has while iterating. V is number of vertices

# Function return total number of paths
def dfsCountPaths(start, target, adjacencyList, visit):
    if (start in visit):
        return 0
    if(start == target):
        return 1
    
    count = 0
    visit.add(start)
    
    for neighbour in adjacencyList[start]:
        count += dfsCountPaths(neighbour, target, adjacencyList, visit)

    visit.remove(start)

    return count


print(dfsCountPaths('A', 'E', {'A': ['B'], 'B': ['C', 'E'], 'C': ['E'], 'E': ['D'], 'D': []}, set()))

start: 'E'
target : 'E'
neighbours: ['C', 'E']

adjanceny: {'A': ['B'], 'B': ['C', 'E'], 'C': ['E'], 'E': ['D'], 'D': []}
