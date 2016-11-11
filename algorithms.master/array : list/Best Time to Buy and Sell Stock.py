'''
Input: [7, 1, 5, 3, 6, 4]
Output: 5

max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)
'''
def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxCur   = 0
        maxSoFar = 0

        for i in range(1, len(prices)):

            profit  = prices[i] - prices[i-1]
            maxCur  = maxCur + profit

            maxCur   = max(0, maxCur)
            maxSoFar = max(maxCur, maxSoFar)

        return maxSoFar


'''
maxCur   = current maximum value
maxSoFar = maximum value found so far
'''
