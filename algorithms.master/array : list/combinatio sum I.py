
def CombinationSum1(candidates, target):

    def combinationSum (candidates, target, res, combination, begin):

        ''' B A S E   C O N D I T I O N '''
        if not target:
            res.append(combination[:])
            return

        ''' R A N G E   O V E R   C A N D I D A T E S '''
        for i in range(begin, len(candidates)):
            if target >= candidates[i]: # if target is still not reached/ just reached
                combination.append(candidates[i])
                # target now is reduced, subtracted one candidate
                combinationSum(candidates, target - candidates[i], res, combination, i)
                combination.pop()

    res         = []
    combination = []
    candidates.sort()
    combinationSum(candidates, target, res, combination, 0)
    return res



def CombinationSum2(candidates, target):

    def combinationSum (candidates, target, res, combination, begin):

        ''' B A S E   C O N D I T I O N '''
        if not target:
            res.append(combination[:])
            return

        ''' R A N G E   O V E R   C A N D I D A T E S '''
        for i in range(begin, len(candidates)):
            if target >= candidates[i] and (candidates[i]!=candidates[i-1] or i==begin): # if target is still not reached/ just reached
                combination.append(candidates[i])
                # target now is reduced, subtracted one candidate
                combinationSum(candidates, target - candidates[i], res, combination, i+1)
                combination.pop()

    res         = []
    combination = []
    candidates.sort()
    combinationSum(candidates, target, res, combination, 0)
    return res

if __name__=="__main__":

    candidates = [2,3,6,7]
    target = 7
    print(CombinationSum2(candidates, target))
