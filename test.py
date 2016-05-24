'''You are given an alphanumeric string.  Write an algorithm that will segment the string into substrings of consecutive integers or numbers and then sort the substrings.  For example,
the string “AZQF013452BAB” will result in “AFQZ012345ABB”.


from itertools import groupby

s = "AZQF013452BAB"
res = []
r = [''.join(g) for _, g in groupby(s, str.isalpha)]
for l in r:
    res.append(''.join(sorted(l)))
print(''.join(res))
'''

s = "AZQF013452BAB"
alpha_list=[]
alpha_list_begin_index = 0

for i,e in enumerate(s):
    if e.isalpha():
        alpha_list_begin_index = i
        alpha_list.append(e)


print(alpha_list)
