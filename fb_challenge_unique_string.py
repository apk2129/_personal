# s = 'abababababababababababababababababab'
#
# # Will contain all the possible substrings
# substrings = set()
#
# # Get all the possible substrings from the main string
# for count in range(0, len(s)):
#    for subStrLen in range(0, len(s) - count):
#        substrings.add(s[count:count + subStrLen + 1])
#
# print(len(substrings))


# s = "()"
#
# stack = []
# for b in s:
#     print( "b",b)
#     if b== '}':
#         if not stack or stack.pop() != '{':
#             print(False)
#     if b== ')':
#         if stack and stack.pop() == '(':
#             continue
#         else:
#             print(False)
#     if b== ']':
#         if not stack or stack.pop() != '[':
#             print(False)
#     else:
#         stack.append(b)
#         print(stack)
#
# print("---",stack)

# if not stack:print(True)
# else: print(False)

times = [[5, 10],[15, 20],[0, 5]]

intervals = (sorted(times))
for i in range(1,len(intervals)):
    print(intervals[i][0],intervals[i-1][1])
    if intervals[i][0] < intervals[i-1][1]:
        print(False)
