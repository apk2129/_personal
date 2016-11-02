from prettytable import PrettyTable


def __print_matrix(grid):
    p = PrettyTable()
    for row in grid:
        p.add_row(row)
    print (p.get_string(header=False, border=False))
