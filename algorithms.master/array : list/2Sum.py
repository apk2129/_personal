nums   = [2, 7, 11, 15]
target = 9

def twoSum( nums, target):
    if len(nums) <= 1 : return False
    diff_map = {}
    for i in range(len(nums)):
       diff = target - nums[i]
       if diff in diff_map:
           return [diff_map[diff],i]
       else:
           diff_map[nums[i]] = i


print(twoSum(nums, target))
