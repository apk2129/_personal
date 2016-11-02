# def romanToInt( s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         romans = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
#
#         num = 0;
#         for i in range(len(s)-1):
#         	# why this condition??
#             print(s[i])
#             if  (romans[s[i]] <  romans[s[i+1]]):
#                 num -= romans[s[i]]
#             else:
#             	num += romans[s[i]]
#
#         return num + romans[s[-1]]
#
# print(romanToInt('MDCCLIV'))
# dfs + stack

# def binaryTreePaths1(self, root):
#     if not root:
#         return []
#     res, stack = [], [(root, "")]
#     while stack:
#         node, ls = stack.pop()
#         if not node.left and not node.right:
#             res.append(ls+str(node.val))
#         if node.right:
#             stack.append((node.right, ls+str(node.val)+"->"))
#         if node.left:
#             stack.append((node.left, ls+str(node.val)+"->"))
#     return res
#

# nums = [2, 7, 11, 15]
# target = 9
#
# diff_map = {}
#
# for i in range(len(nums)):
# 	diff = target - nums[i]
# 	if diff in diff_map:
#         print("!")3[diff_map[diff],i])
#     else:
#         diff_map[diff] = i
#
# print(diff_map)

def print_m( ms ):
	for matrix in ms:
		for i in matrix:
			print(i)
		print("------")


A = [[ 1, 0, 0],[-1, 0, 3]]
B = [[ 7, 0, 0 ],[ 0, 0, 0 ],[ 0, 0, 1 ]]

ma = len(A)
na = len(A[0])

mb = len(B)
nb = len(B[0])

if na != mb : raise Exception(" m != n")

AB =[[0 for _ in range(nb)] for _ in range(ma)]

print_m([A,B,AB])

for i, row in enumerate(A):
	print(i,row)
	for k, eleA in enumerate(row):
		if eleA: # only non zero
			for j, eleB in enumerate(B[k]):
				if eleB:
					AB[i][j] += eleA * eleB

print([AB])
