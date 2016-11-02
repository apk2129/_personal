from collections import defaultdict
import pprint

def lszero(A):
        N = len(A)
        pre = [None]*N
        curr = 0
        for i in range(N):
            curr += A[i]
            pre[i] = curr

        print(pre) # cummulative sum [1, 3, 1, 5, 1]


        seen_table = defaultdict(list)
        seen_table[0]=[-1]
        longest = -1
        indices = None
        pprint.pprint(seen_table)
        for i in range(N):
            s = pre[i]
            seen_table[s].append(i)
            pprint.pprint(seen_table,width=2)
            gap = seen_table[s][-1] - seen_table[s][0]
            if gap > longest:
                longest = gap
                indices = (seen_table[s][0]+1,seen_table[s][-1]+1)
        if indices:
            return A[indices[0]:indices[1]]
        else:
            return []


print(lszero([1,2,-2,4,-4]))



def getinterval(l):

	l.sort(key=lambda x: x[0])
	print(l)
	result = l[0][1] - l[0][0]

	for i in range(1,len(l)):

		if l[i][1]<=l[i-1][1]: continue
		elif l[i][1]>l[i-1][1] and l[i][0]>l[i-1][1]:
			result += l[i][1] - l[i][0]
		else:
			result += l[i][1] - l[i-1][1]

	return result
