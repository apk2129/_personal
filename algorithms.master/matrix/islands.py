from prettytable import PrettyTable

''' m a x i m u m s u b - s q u a r e '''

def maximum_sub_square(grid):

    print("copy")
    result = [
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0]]

    for k1,v1 in enumerate(grid):
        print(k1)
        print(v1)
        for k2, v2 in enumerate(v1):
            if v2 == 0:
                result[k1][k2] = 0
            else:
                new_value = get_minimum_value(result, k1, k2) + 1
                result [k1][k2] = new_value

        __print_matrix(result)

        # for element_index, element in row:
        #     print(row, element)
    print("result")
    __print_matrix(result)

def get_minimum_value(grid, row_index, element_index):

    min_val = min(grid[row_index][element_index-1],
    grid[row_index-1][element_index] ,
    grid[row_index-1][element_index-1])
    print("min_val",min_val)
    return min_val



def __print_matrix(grid):
    p = PrettyTable()
    for row in grid:
        p.add_row(row)
    print (p.get_string(header=False, border=True))

if __name__=="__main__":

    grid = [
        [0,1,1,0,1],
        [1,1,1,0,0],
        [1,1,1,1,0],
        [1,1,1,0,1]]

    print("original grid")
    __print_matrix(grid)

    (maximum_sub_square(grid))
