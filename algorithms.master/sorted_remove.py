# def removeDuplicates( nums ):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         if not nums : return 0
#         write_index = 1
#         for i in range(1,len(nums)):
#
#             if nums[i-1]!= nums[i]:
#                 nums[write_index] = nums[i]
#                 write_index += 1
#             print(nums)
#             print(write_index)
#
#         return write_index
#
# print(removeDuplicates([1,2,3,3,3,44]))

def removeDuplicates( nums, k):
    i = 0
    for n in nums:
        if i < k or n > nums[i-k]:
            nums[i] = n
            i += 1
        print(nums)

    return i

print(removeDuplicates([1,2,3,3,3,4,4,4,4,4,5], 3))
