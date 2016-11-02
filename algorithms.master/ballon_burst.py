from functools import reduce
import sys
class Solution(object):

    result = 0
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        x = len(nums)
        while(x):
            print("nums before burst : " , nums)
            sub_nums    = nums[:3]
            nums        = nums[3:]
            nums        = self.burst(sub_nums) + nums
            print("nums after burst : " , nums)
            print("-----------------")
            x -= 1
        return self.result

    def burst(self, sub_nums
        print("burst : ", sub_nums)
        if len(sub_nums)==1 :
            print("burst : ", sub_nums)
            self.result += sub_nums[0]
            sub_nums.pop(0)
            return sub_nums
        if len(sub_nums)==2 :
            self.result += (sub_nums[0]*sub_nums[1])
            sub_nums.pop(0)
        else:
            self.result +=  reduce(lambda x, y: x*y,sub_nums)
            sub_nums.pop(1)

        print(self.result)
        return sub_nums


if __name__=="__main__":
    s = Solution()
    print(s.maxCoins([9,76,64,21]))
    print(s.result)
