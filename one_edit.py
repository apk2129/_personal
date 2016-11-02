import math

def one_edit(s,t):

    # aaple : baple    # replace
    # aaple : aapl     # remove
    # aaple : apples   # add

    if math.fabs(len(s) - len(t)) > 1 : return False

    if len(s) == len(t):
        return isModify(s,t)
    elif len(s) > len(t):
        return isRemove(s,t)
    else:
        return isRemove(t,s)


def isModify( s , t ):
    diff = 0
    for i in range(len(s)):
        if s[i]!=t[i]:
            diff += 1

    return diff == 1

def isRemove( s , t ):
    print("s",s)
    print("t",t)
    i= 0
    j = 0
    while i<len(s) and j<len(t):
        print(s[i],t[j])
        if s[i] != t[j]:
            return s[i+1:]==t[j:]
        i += 1
        j += 1

    return True




print(one_edit("ANISH","ANRT"))
print("anishkelkar"[:-4])
