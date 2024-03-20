
# Time Complexity
from collections import deque


def countPathsInGrid(grid, start, target):
    
    queue = deque()
    queue.append(start)
    
    visit = set()
    visit.add(start)

    pathLength = 0


    while len(queue) != 0:

        for i in range(len(queue)):
            currentPosition = queue.popleft()
            if(currentPosition == target):
                return pathLength
            
            for neighbour in getNeighbours(currentPosition):
                if (outOfBounds(neighbour, grid) or visited(neighbour, visit) or blocked(neighbour, grid)):
                    continue
                queue.append(neighbour)
                visit.add(neighbour)

        pathLength+=1


    return pathLength






#Helper Functions
def outOfBounds(position, grid):
    r, c = position
    if(r < 0 or c < 0):
        return True
    if(c > len(grid[0]) - 1 or r > len(grid) - 1):
        return True
    return False


def visited(position, visit):
    if position in visit:
        return True
    return False

def blocked(position, grid):
    if grid[position[0]][position[1]] == 1:
        return True
    return False

def getNeighbours(position):
    r,c = position
    return [
        (r + 1, c),
        (r - 1, c),
        (r, c + 1),
        (r, c - 1),
        ]



#MAIN Call
grid =  [
     [0,0,0,0],
     [1,1,0,0],
     [0,0,0,1],
     [0,1,0,0],
    ]

target= (3,3)

start = (0,0)


print(countPathsInGrid(grid, start, target))