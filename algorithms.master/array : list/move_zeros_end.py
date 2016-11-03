nums = [0,1,0,3,12]
current = 0;
for i in range(0,len(nums)):
    print(nums,current)
    if (nums[i] != 0):
        nums[current] = nums[i]
        current += 1

'''
at this point the pointer is at the last nonzero element
all non zero elements have been shifted
there will be dupicates towards the  end after the pointer
nums = [ 1 , 3 , 12 , 3 , 12]
                      ^
                current pointer
now from this location till end append all Z E R O E S
'''

for i in range(current,len(nums)):
    nums[i] = 0

#nums.sort(key= lambda x: 1 if x == 0 else 0)

print(nums)
