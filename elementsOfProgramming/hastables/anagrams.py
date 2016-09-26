
l = ["debitcard", "elvis", "silent", "badcredit", \
     "lives", "freedom", "listen", "levis", "money"]


d = {}

for e in l:
    key = ''.join(sorted(list(e)))
    if key not in d:
        d[key]= [e]
    else:
        d[key].append(e)

import pprint
pprint.pprint(d)



l = [1,1,2,3,4]
print(set('aaaaaanigh'))
