class Solution(object):
    def orangesRotting(self, grid):
        """
        :type nums: List[int]
        :rtype: int
        """
        time_elapsed = -1
        rotten_orange_positions = []

        if (self.fresh_oranges_not_exist(grid)):
            return 0
            

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if(grid[r][c] == 2):
                    rotten_orange_positions.append((r,c))
                    
                    
        time_elapsed = self.multi_source_bfs(grid,rotten_orange_positions)
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if(grid[r][c] == 1):
                    return -1
                
        return time_elapsed
        

    def fresh_oranges_not_exist(self, grid):
        fresh_oranges = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if(grid[r][c] == 1):
                    fresh_oranges+=1
        if(fresh_oranges == 0):
            return True
        return False

    def multi_source_bfs(self, grid, positions):

        minutes_elapsed = -1

        
        queue = deque()
        visit = set()
        
        for position in positions:
           
            queue.append(position)

            visit.add(position)
            

        while len(queue) != 0:

            for i in range(len(queue)):

                current_position = queue.popleft()

                for neighbour in self.get_neighbours(current_position):
                    
                    if(self.out_of_bounds(grid, neighbour) or self.visited(visit, neighbour) or self.blocked(grid, neighbour)):
                        continue
                    

                    queue.append(neighbour)
                    visit.add(neighbour)
                    grid[neighbour[0]][neighbour[1]] = "r"

           
            minutes_elapsed +=1
        return minutes_elapsed 


    def visited(self, visit, position):
        if position in visit:
            return True
        return False
    
    
    def out_of_bounds(self, grid, position):
        r,c = position
        if(r < 0 or c < 0):
            return True
        if(r > (len(grid) - 1) or c > (len(grid[0]) - 1)):
            return True
        return False


    def get_neighbours(self, position):
        r , c = position
        return [
            (r + 1,c),
            (r - 1,c),
            (r, c + 1),
            (r, c - 1)
        ]
    
    def blocked(self, grid, position):
        r ,c = position
        if (grid[r][c] == 0):
            return True
        return False

        

 


sol = Solution()

grid = [[2,1,1],
        [1,1,0],
        [0,1,1]]

grid2 = [[2,1,1],
         [0,1,1],
         [1,0,1]]

grid3 = [[0,2,2]]

grid4 = [[0]]

grid5 = [[2,1,1],
         [1,1,1],
         [0,1,2]]

print(sol.orangesRotting(grid2))


#  [1,2,3]
#     /\
    
# 1 + 3  2
         
    


