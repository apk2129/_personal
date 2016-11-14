def generatePalindromes( s ):
    """
    :type s: str
    :rtype: List[str]
    """
    res      = []
    chardict = {}

    '''build char dict'''
    for char in s: chardict[char] = chardict.get(char,0) + 1

    print(chardict)


    ''' separate odd occurring character
        Palindrome can have only one ODD character
    '''
    numodd = 0
    odd_char = ''

    for i in chardict:
        if chardict[i] %2 == 1:
            numodd   += 1
            odd_char += i

    if numodd > 1: return []
    else:
        if numodd == 1: chardict[odd_char] -= 1
        permutations(chardict,len(s), '', odd_char, res)
    return res

def permutations( chardict, n , st, odd_char, res):
    print( "chardict ",chardict, " n ", n , "  st :",st,"     odd_char: ", odd_char, res)
    if len(st) == n/2:
        print("----",res)
        res.append( st+odd_char+st[::-1])
        return
    else:
        for i in chardict:
            if chardict[i] > 0 :
                chardict[i] -= 2
                permutations(chardict, n, st+i, odd_char, res)
                chardict[i] += 2

print(generatePalindromes("abbacc"))
