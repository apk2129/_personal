N = 4
SQN =2

def FindUnassignedLocation(grid):
    for row in range(N):
        for col in range(N):
            if (grid[row][col] == 0):
                return [row,col]
    return False

def SolveSudoku(grid):

	loc = FindUnassignedLocation(grid)
	# if there is no unaaasinged location left you are done!
	if not loc:
		return True
	row,col = loc

	# consider digits 1 to 9
    for num in range(1,10):
    	if isSafe(grid, row, col, num):
            # make tentative assignment
            grid[row][col] = num

            #return, if success, yay!
            if SolveSudoku(grid):
                return True

            #failure, unmake & try again
            grid[row][col] = 0

    return False # this triggers backtracking


def isSafe(grid, row, col, num):
    # /* Check if 'num' is not already placed in current row,
    #    current column and current 3x3 box */
    return !UsedInRow(grid, row, num) and !UsedInCol(grid, col, num) and !UsedInBox(grid, row - row%SQN , col - col%SQN, num)
def UsedInRow(grid, row, num):
    for col in range(N)
        if (grid[row][col] == num):
            return True
    return False
def UsedInCol(grid, row, num):
    for col in range(N)
        if (grid[row][col] == num):
            return True
    return False
def UsedInBox(grid, boxStartRow, boxStartCol, num):

    SQN = 2
    for row in range(SQN):
        for col in range(SQN):
            if (grid[row+boxStartRow][col+boxStartCol] == num):
                return True
    return False

def FindUnassignedLocation(grid):
    for row in range(N):
        for col in range(N):
            if grid[row][col] == 0:
                return [row,col]
    return False


grid        = [[0,0,3,4],
               [3,4,0,0],
               [0,0,4,3],
               [0,3,2,0]]

if  SolveSudoku(grid) == True :
      printGrid(grid)
else:
     print("No solution exists")
