# st = list('anprish')
# l = len(st)
# for i in range(0, l//2):
#     st[i], st[l-1-i] = st[l-1-i], st[i]
#
# print(''.join(st))


# ----------------------------------------------

s = 'asbp'

def permutations(s):

    for j in range(len(s)):
        print(s[j])
        new = s[:j] + s[j+1:]
        for i in range(len(s)):
            print(new[:i] + s[j] + new[i:])

print(permutations(s))


#---------------------------------


s1 = [x for x in range(1,11)]
s2 = [x for x in range(1,10)]

diff = sum(s1) -sum(s2)
