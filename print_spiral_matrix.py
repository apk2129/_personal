
'''
MATRIX  M X N

TOP ROW OF UNTRAVERSED ARRAY     T = 0
BOTTOM ROW OF UNTRAVERSED ARRAY  B = M - 1
LEFT ROW OF UNTRAVERSED ARRAY    L = 0
RIGHT ROW OF UNTRAVERSED ARRAY   R = N -1

T - > 1  2  3
      8  9  4
B - > 7  6  5
      ^     ^
      L     R

ALGORITHM :  START WITH DIRECTION = 0 , TRAVESER TOP MOST THEN CHANGE DIRECTION = 1 AND CONTINUE

'''
def print_spiral ( matrix , m , n):

    T = 0
    B = m - 1
    L = 0
    R = n -1
    dir = 0 # * * * I M P O R T A N T !

    result = []

    while T<=B and L<=R:

        if dir == 0 : # TRAVERSE TOPMOST ROW      T
            for i in range( L , R + 1 ): result.append(matrix[T][i])
            T += 1 # ONCE TRAVERSED , DISCARD THE ROW --> SET NEW TOPMOST ROW
            # dir = 1

        elif dir == 1: # TRAVERSE TOP TO BOTTOM    R
            for i in range( T , B + 1 ): result.append(matrix[i][R])
            R -= 1
            # dir = 2

        elif dir == 2: # TRAVERSE RIGHT TO LEFT    B
            for i in range( R , L - 1 , - 1 ): result.append(matrix[B][i])
            B -= 1
            # dir = 3

        elif dir == 3: # TRAVERSE BOTTOM TO UP     L
            for i in range( B , T - 1 , - 1 ): result.append(matrix[i][L])
            L += 1
            # dir = 0

        dir = ( dir + 1 ) % 4


    print(result)



print_spiral([[1,2,3],
              [8,9,4],
              [7,6,5]],3,3)
