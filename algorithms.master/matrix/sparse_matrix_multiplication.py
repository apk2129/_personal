def print_m(ms):
    for matrix in ms:
        for i in matrix:
            print(i)


def sparse_matrix_multiply(A, B):

    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])

    if cols_A != rows_B:
        raise Exception(" m != n")

    AB = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

    for i, row in enumerate(A):
        for k, eleA in enumerate(row):
            if eleA:  # only non zero
                for j, eleB in enumerate(B[k]):
                    if eleB:
                        AB[i][j] += eleA * eleB

    return AB


def matrix_multiply(A, B):

    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])

    if cols_A != rows_B:
        raise Exception(" m != n")

    AB = [[0 for _ in range(cols_B)] for col in range(rows_A)]

    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                AB[i][j] += A[i][k] * B[k][j]

    return AB


if __name__ == "__main__":

    A = [[1, 0, 0],
         [-1, 0, 3]]

    B = [[7, 0, 0],
         [0, 0, 0],
         [0, 0, 1]]

    print_m([matrix_multiply(A, B)])
    print_m([sparse_matrix_multiply(A, B)])
