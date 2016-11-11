result= []
import collections
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
if not strs : print(result)
mp = collections.defaultdict(list)
for s in strs:
    k = ''.join(sorted(s))
    mp[k].append(s)

for k,v in mp:
    print(v)
    result.append(v)

print(result)
