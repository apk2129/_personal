def romanToInt( s):
        """
        :type s: str
        :rtype: int
        """
        romans = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

        num = 0;
        for i in range(len(s)-1):

            if  (romans[s[i]] <  romans[s[i+1]]):
                num -= romans[s[i]]
            else:
            	num += romans[s[i]]

        return num + romans[s[-1]]


def intToEnglish ( n ):
    pass



if __name__ == "__main__":

    print(romanToInt('MDCCLIV'))
    print(intToEnglish(romanToInt('MDCCLIV')))
