# Time: O(N^V)
# where N is number of choices each node has while iterating. V is number of vertices

# Function return shortest path to the target
from collections import deque


def bfsCountPaths(start, target, adjacencyList):

    pathLength = 0

    queue = deque()
    queue.append(start)

    visit = set()
    visit.add(start)

    while len(queue) != 0:


        for i in range(len(queue)):

            currentNode = queue.popleft()
            print(adjacencyList[currentNode], currentNode, pathLength)

            if(currentNode == target):
                return pathLength
            
            for neighbour in adjacencyList[currentNode]:

                if(neighbour not in visit):
                    queue.append(neighbour)
                    visit.add(neighbour)

        pathLength+=1


    return pathLength

#pathLength = 3
print(bfsCountPaths('A', 'D', {'A': ['B'], 'B': ['E', 'C'], 'C': ['E'], 'E': ['D'], 'D': []},))


