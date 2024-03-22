# Time: O(n * m), Space: 0(m), where m is num of cols

# Returns Total number of Paths from top to bottom in a two dimentional grid

def uniquePaths(self, rows, cols):

    previous_row = [0] * cols
    
    for row in range(rows - 1, -1, -1):
        
        current_row = [0] * cols
        current_row[cols - 1] = 1

        for col in range(cols - 2, -1, -1):
            current_row[col] = current_row[col + 1] + previous_row[col]
    
        previous_row = current_row

    return previous_row[0]



print(uniquePaths(4,4 ))
