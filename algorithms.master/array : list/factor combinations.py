def getFactors (n):
    result = []
    temp = []
    getResult(n, 2, temp, result)
    return result

def getResult(num, start, currentResult, finalResult):
    import copy
    if (num == 1):
        if (len(currentResult) > 1):
            # x= copy.deepcopy()
            finalResult.append(currentResult[:]) #<------- importatn for deep copy !!
        return

    for i in range(start, num+1):
        if (num%i == 0):
            currentResult.append(i)
            getResult(num//i, i, currentResult, finalResult)
            currentResult.pop()


print(getFactors(12))
