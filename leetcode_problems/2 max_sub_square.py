from prettytable import PrettyTable

''' m a x i m u m s u b - s q u a r e
maximum size sub square matric with all 1's
'''


def maximum_sub_square(grid):

    result=[]
    max=0
    for n in grid:
        result.append([0]*len(n))

    '''copy first row'''
    result[0] = grid[0]
    '''copy first column'''
    for k, v in enumerate(grid):
        result[k][0] = grid[k][0]

    for k1, v1 in enumerate(grid):
        for k2, v2 in enumerate(v1):
            if v2 == 0:
                result[k1][k2] = 0
            else:
                print(k1,k2)
                new_value = get_minimum_value(result, k1, k2) + 1
                max = new_value if new_value>max else max
                result [k1][k2] = new_value

    return max

'''--------------------------------------------------------------------------'''
def get_minimum_value(grid, row_index, element_index):

    min_val = min(grid[row_index][element_index-1],
    grid[row_index-1][element_index] ,
    grid[row_index-1][element_index-1])
    return min_val

def __print_matrix(grid):
    p = PrettyTable()
    for row in grid:
        p.add_row(row)
    print (p.get_string(header=False, border=True))

if __name__=="__main__":
    grid = [
        [1,1,1,1,1],
        [1,1,1,1,0],
        [1,1,1,1,0],
        [0,0,0,0,0]]

    print(maximum_sub_square(grid))
