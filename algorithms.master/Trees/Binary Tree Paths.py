
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
