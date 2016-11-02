'''ctci 1.6 String compression'''

s = 'aaaaaabbbbccccccc'

from collections import Counter

r = ''

for k,v in Counter(s).items():
    r += k + str(v)

print(r)
