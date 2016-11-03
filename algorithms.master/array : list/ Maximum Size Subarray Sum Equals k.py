'''
Preprocess the input array such that you get the range sum in constant time.
sum[i] means the sum from 0 to i inclusively
the sum from i to j is sum[j] - sum[i - 1] except that from 0 to j is sum[j].
'''
nums = [1, -1, 5, -2, 3 ]
k    = 3

ans, acc = 0, 0               # answer and the accumulative value of nums
mp = {0:-1}                 #key is acc value, and value is the index
for i in range(len(nums)):

    acc += nums[i]

    if acc not in mp:
        mp[acc] = i
    '''
        now check if target - nums[i] in map
        “if acc-k in mp:” is to find whether there's a subarray with sum of k;
        and mp[acc-k] has the starting index of that subarry,
        and thus i-mp[acc-k] is the length of the subarray.
    '''
    if acc-k in mp:
        ans = max(ans, i-mp[acc-k])

print(ans)


import pprint
pprint.pprint(mp, width =2)
