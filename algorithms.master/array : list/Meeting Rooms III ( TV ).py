'''--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
T V ROOM  CAREER CUP
There's a room with a TV and people are coming in and out to watch it. The TV is on only when there's at least a person in the room. For each person that comes in, we record the start and end time. We want to know for how long the TV has been on. In other words: Given a list of arrays of time intervals, write a function that calculates the total amount of time covered by the intervals.
For example:
# input = [(1,4), (2,3)]  # > 3
# input = [(4,6), (1,2)]  # > 3
# input = [(1,4), (6,8), (2,4), (7,9), (10, 15)]  # > 11

'''-- sorted list ---'''
1 4               result = 4-1 = 3
2 4     case I    --ignore
6 8     case II   result = 3 + (8 - 6)   = 5
7 9     case III  result = 5 + (9 - 8)   = 6
10 15   case II   result = 6 + (15 - 10) = 11

'''
def getinterval(l):

    ''' sort tuple-list according to starting times '''
    l.sort(key=lambda x: x[0])

    ''' Store result of first start - end'''
    result = l[0][1] - l[0][0]

    for i in range(1, len(l)):

        if l[i][1] <= l[i - 1][1]:                            # case I
            continue
        elif l[i][1] > l[i - 1][1] and l[i][0] > l[i - 1][1]: # case II
            result += l[i][1] - l[i][0]
        else:
            result += l[i][1] - l[i - 1][1]                   # case III

    return result
