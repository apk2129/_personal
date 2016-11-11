'''maximum contiguous sub array
http://www.geeksforgeeks.org/largest-sum-contiguous-subarray/'''

# l = [-2,1,-3,4,-1,2,1,-5,4]
l=[-1,-2,-3,-11]


max_so_far = 0
max_ending_here =0

''' for all negative number'''
if max(l)<0 :
    print(max(l))


'''Algorithm doesn't work for all negative numbers.
It simply returns 0 if all numbers are negative.
For handling this we can add an extra phase before actual implementation.
The phase will look if all numbers are negative,
if they are it will return maximum of them (or smallest in terms of absolute value).
There may be other ways to handle it though.
'''
for e in l:
    max_ending_here += e
    if max_ending_here < 0:
        max_ending_here = 0
    elif max_ending_here > max_so_far:
         max_so_far = max_ending_here

print(max_so_far)


'''------------ another leetcode solution ---'''
nums=[-2,1,-3,4,-1,2,1,-5,4]
for i in range(1, len(nums)):
        if nums[i-1] > 0:
            nums[i] += nums[i-1]
print(max(nums))
