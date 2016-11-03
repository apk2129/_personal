 # https://discuss.leetcode.com/topic/14288/python-o-n-and-o-n-log-n-solution
nums = [2,3,1,2,4,3, 7]
s    = 7

'''
    [ 2 , 3 , 1 , 2 , 4 , 3 ]
      ^
    left

'''

left   = 0
total  = 0
result = len(nums) + 1



for right , n in enumerate(nums):

    total += n
    '''
        [ 2 , 3 , 1 , 2 , 4 , 3 ]
          ^           ^
        left         right

    '''
    while total >= s:

        subaray_len = right - left + 1
        result      = min(subaray_len, result)

        total = total - nums[left]
        left  = left + 1
        '''
                [ 2 , 3 , 1 , 2 , 4 , 3 ]
                      ^       ^
                     left    right

        '''

if result > len(nums): result =  0

print(result)
