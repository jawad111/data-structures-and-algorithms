
# Time Complexity
def countPathsInGrid(grid, start, target, visit):
    if (outOfBounds(start, grid) or visited(start, visit) or blocked(start, grid)):
        return 0
    
    if(start == target):
        return 1
    


    visit.add(start)

    count = 0

    count+= countPathsInGrid(grid, (start[0] + 1, start[1]),target, visit)
    count+= countPathsInGrid(grid, (start[0] - 1, start[1]),target, visit)
    count+= countPathsInGrid(grid, (start[0], start[1] + 1),target, visit)
    count+= countPathsInGrid(grid, (start[0], start[1] - 1),target, visit)



    visit.remove(start)


    return count







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


grid =  [
     [0,0,0,0],
     [1,1,0,0],
     [0,0,0,1],
     [0,1,0,0],
    ]

target= (3,3)

start = (0,0)

#MAIN Call
print(countPathsInGrid(grid, start, target, set()))