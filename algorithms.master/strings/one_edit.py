import math

def one_edit(s,t):

    # aaple : baple    # replace
    # aaple : aapl     # remove
    # aaple : apples   # add

    if math.fabs(len(s) - len(t)) > 1 or s==t : return False

    if len(s) == len(t):
        return isModify(s,t)
    elif len(s) > len(t):
        return isRemove(t,s)
    else:
        return isRemove(s,t)


def isModify( s , t ):
    diff = 0
    for i in range(len(s)):
        if s[i]!=t[i]:
            diff += 1

    return diff == 1

def isRemove( short , long ):
    # s length is always S M A L L E R
    for i in range(len(short)):
        if short[i] != long[i]:
            '''if not equal it could be removed or added'''
            return short[i:] == long[i+1:]

    return True




print(one_edit("ANISH","ANISH"))



'''
def isOneEditDistance(self, s, t):
    if len(s) > len(t):
        return self.isOneEditDistance(t, s)
    if abs(len(s) - len(t)) > 1 or s == t:
        return False
    for i in range(len(s)):
        if s[i] != t[i]:
            return s[i+1:] == t[i+1:] or s[i:] == t[i+1:]
    return True
'''
