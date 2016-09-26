'''
Write a function to compute a simple moving average (SMA) of a list of numbers, e.g. 1 to 10.
The function should accept a window length, e.g. 3. What would be some optimizations?
'''

import random
import pprint
import cProfile

def f(list_of_numbers, window):

    chunk = []
    final = []

    for i in range(0,len(list_of_numbers)-1):
        chunk.append(list_of_numbers[i])
        if (i+1)%3==0:
            final.append(chunk)
            chunk = []

    for wind in final:
        print(wind, sum(wind) / float(len(wind)))





if __name__=="__main__":

    l = random.sample(range(10000),25)
    cProfile.run('f(l, 3)')
    # timeit.Timer('f(l,3)', 'gc.enable()').timeit()
