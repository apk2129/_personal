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

        for i in range(N): #[1,2,-2,4,-4]
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
