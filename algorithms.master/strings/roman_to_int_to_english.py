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

lessThan20 = ["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
tens = ["","Ten","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]
thousands = ["","Thousand","Million","Billion"]

def intToEnglish ( num ):
    if num == 0:
        return "Zero"
    res = ""
    for i in range(len(thousands)):
        if num % 1000 != 0:
            res = helper(num%1000) + thousands[i] + " " + res
        num = num // 1000
    return res.strip()

def helper(num):

    if num == 0:
        return ""
    elif num < 20:
        return lessThan20[num] + " "
    elif num < 100:
        return tens[num//10] + " " + lessThan20[num%10] ########
    else:
        return lessThan20[num//100] + " Hundred " + helper(num%100)



if __name__ == "__main__":


    print(romanToInt('MDCCLIV'))
    print(intToEnglish(123456789))
