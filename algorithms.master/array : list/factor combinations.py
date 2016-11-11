import math
def factorCombinations(no):

    def helper(result, n , start, element, upper):
        print(result)
        if n == 1 and len(element) > 1:
            result.append(element)
            return

        for i in range(start, n+1):
            if i > upper:
                i = n
            if n%i == 0:
                element.append(i)
                helper(result, n//i,i,element,math.sqrt(n//i) )
                element.pop(-1)

    result = [[]]
    element = []
    helper(result,no , 2, element, math.sqrt(no) )
    return result

print(factorCombinations(6))
