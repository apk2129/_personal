'''Given an unsorted array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....

Example:
(1) Given nums = [1, 5, 1, 1, 6, 4], one possible answer is [1, 4, 1, 5, 1, 6].
(2) Given nums = [1, 3, 2, 2, 3, 1], one possible answer is [2, 3, 1, 3, 1, 2].'''



nums = [1, 5, 1, 1, 6, 4]

for i, value in enumerate(nums):
    if i%2==0:
        #odd index
        if nums[i] < nums[i-1]:
            swap(i)
    elif i%2==0 and i != 0:
        #even index
        if nums[i-1] < nums[i]:
            swap(i)

        
