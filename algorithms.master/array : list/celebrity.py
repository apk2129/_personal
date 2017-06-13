p = [0,1,2,3,4,5,6,7]
def findCelebrity(self, n):
    x = 0
    for i in xrange(n):
        if knows(x, i):
            x = i
    if any(knows(x, i) for i in xrange(x)):
        return -1
    if any(not knows(i, x) for i in xrange(n)):
        return -1
    return x
'''
The first loop is to exclude n - 1 labels that are not possible to be a celebrity.
After the first loop, x is the only candidate


The second and third loop is to verify x is actually a celebrity by definition.

The key part is the first loop. To understand this you can think the knows(a,b) as a a < b comparison, if a knows b then a < b, if a does not know b, a > b. Then if there is a celebrity, he/she must be the "maximum" of the n people.

'''

int x = 0
for (int i = 0; i < n; ++i) if (knows(x, i)) x = i;
for (int i = 0; i < x; ++i) if (knows(x, i)) return -1;
for (int i = 0; i < n; ++i) if (!knows(i, x)) return -1;
return x
