# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

# Example 1:

# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
# Example 2:

# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3
 


import copy


class Solution(object):
    def n(self, grid):
        """
        :type nums: List[int]
        :rtype: int
        """
        islands = 0
        visit = set()
        print(len(grid))

        for i in range(len(grid)):
    
            for j in range(len(grid[0])):
    
                
                if(grid[i][j] == "1"):
                    islands +=1
                    grid = self.explore_island(grid, (i,j), visit)


        return islands
    

    def explore_island(self, grid, start, visit):
        if (self.outOfBounds(start, grid) or self.visited(start, visit) or self.is_water(start, grid)):
            return 
        
        if(self.is_land(start, grid) and (not self.visited(start, visit))):
            grid[start[0]][start[1]] = 0
   

        visit.add(start)


        self.explore_island(grid, (start[0] + 1, start[1]), visit)
        self.explore_island(grid, (start[0] - 1, start[1]), visit)
        self.explore_island(grid, (start[0], start[1] + 1), visit)
        self.explore_island(grid, (start[0], start[1] - 1), visit)



        #visit.remove(start)


        return grid




    #Helper Functions
    def outOfBounds(self, position, grid):
        r, c = position
        if(r < 0 or c < 0):
            return True
        if(c > len(grid[0]) - 1 or r > len(grid) - 1):
            return True
        return False


    def visited(self, position, visit):
        if position in visit:
            return True
        return False

    def is_land(self, position, grid):
        if grid[position[0]][position[1]] == "1":
            return True
        return False
    
    def is_water(self, position, grid):
        if grid[position[0]][position[1]] == "0":
            return True
        return False


 








 
    
sol = Solution()

area1 = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
area2 = [["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]]

area3 = [["1"]]

print(sol.n(area2))


#  [1,2,3]
#     /\
    
# 1 + 3  2
         
    


