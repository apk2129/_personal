nums= [1,1,-2]
# nums= [-1, 0, 1, 2, -1, -4]
target = 0

result =  []
nums = sorted(nums)
for i in range(len(nums)-3):

    target = -nums[i]
    lo = i + 1
    hi = len(nums) - 1

    while lo<hi:
        sum = nums[lo] + nums[hi]
        if   sum < target:  lo += 1
        elif sum > target:  hi -= 1
        else:
            result.add([nums[i],nums[lo],nums[hi]])
            break

print(result)
