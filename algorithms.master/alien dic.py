import collections
import pprint

words = [
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]
# convert the above input to adjust list

adj = collections.defaultdict(set)

for word in words:
    adj[word[0]].append()word[1:])

print(adj)




adj = {
    'E' : ['R','T'],
    'W' : ['R'],
    'R' : ['T', 'F'],
    'T' : [],
    'F' : ['T']
}

in_degree = collections.defaultdict(int)
queue     = []
result    = []


# ------------------  compute in degrees
for v,edges in adj.items():
    if not v in in_degree: in_degree[v] = 0     # for 0 in degrees to be considered else not inserted in indegree map
    for e in edges: in_degree[e] += 1

# {'T': 3, 'W': 0, 'R': 2, 'E': 0, 'F': 1}

# ------------------  get indegree==0 in queue
for e,v in in_degree.items():
    if v ==0 :
        queue.append(e)
        result.append(e)

# ------------------ dfs
while queue:
    edge = queue.pop()
    out  = adj[edge]
    if out:
        for i in out:
            in_degree[i] -= 1       # decrement in dree
            if in_degree[i] == 0 :  # after decrementing if indegree== 0 means all predecessor done
                queue.append(i)     # now append to queue for subsequent investigacation
                result.append(i)    # also append to final result



print("result ", result)
