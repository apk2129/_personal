''' CTCI SOLUTION '''
import copy

class ChessBoard(object):

    def __init__(self, n):
        '''initialize n x n ChessBoard
        '''
        self.queens = dict()
        self.size = n

    def place(self, row, column):
        self.queens[row] = column

    def is_free(self, row, column):
        """ Check whether (row, column) is a valid square for a new queen.
        Returns False in case there already is a queen placed on the same row,
        column or diagonal; True otherwise. In other words: this method tells
        us if a new queen can be placed on the board without being threatened
        by one of the existing queens."""

        for x, y in self.queens.items():

            if x == row:
                return False

            if y == column:
                return False

            ''' D I A G O N A L   C O N D I T I O N '''
            # Two queens are in the same diagonal if the distance between
            # the rows is the same as the distance between the columns.
            if abs(row - x) == abs(column - y):
                return False

        return True #valid position

    @classmethod
    def queens_nways(cls, n, board=None, row=0, remaining=None):

        if not board:
            board = cls(n)

        if remaining is None:
            remaining = board.size

        # All queens placed
        if not remaining:
            return 1

        total = 0
        for column in range(board.size):
            if board.is_free(row, column):
                board_copy = copy.deepcopy(board)
                board_copy.place(row, column)
                total += cls.queens_nways(n, board_copy, row + 1, remaining - 1)
        return total




if __name__ == '__main__':

    print(ChessBoard.queens_nways(8))
