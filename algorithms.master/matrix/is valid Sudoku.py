
def isValidSudoku(self, board):
    """
    :type board: List[List[str]]
    :rtype: bool
    """
    for i,row in enumerate(board):
        for j,element in enumerate(row):
            if board[i][j] != ".":
                if not self.isValid(board,i,j,board[i][j]):
                    return False
    return True

def isValid(self, board, row , col , c ):

    # duplicate in row
    for i in range(9):
        if board[row][i] == c and i!=col:
            return False

    # duplicate in col
    for j in range(9):
        if board[j][col] == c and j!=row:
            return False

    # duplicate in box
    box_start_row = row - row%3  # get box start row + col
    box_start_col = col - col%3
    for brow in range(box_start_row, box_start_row+3):
        for bcol in range(box_start_col, box_start_col+3):
            if (board[brow][bcol] == c):
                if brow != row and bcol != col:
                    return False
    return True
