class Solution(object):

    def majorityElement(self, nums):
        if not nums : return 0
        length = len(nums)/2
        dict= {}
        for n in nums:
            if n in dict:
                dict[n]+=1
            else:
                dict[n] = 1

        for key, val in dict.items():
            if val>length:
                return key


        return "no major element"

    def major(self, nums):

        for n in nums:
            if (nums.count(n) > len(nums)/2):
                return n


if __name__ == "__main__":

    l = [2,3,34,5,5,6,6,6,6,6,6,6]
    S = Solution()
    print(S.majorityElement(l))
    print(S.major(l))
#
