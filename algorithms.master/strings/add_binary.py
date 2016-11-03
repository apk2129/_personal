a = "11"
b = "1"
#Return "100"


def addBinary(a, b):
    """
     :type a: str
     :type b: str
     :rtype: str
    """
    m = len(a)
    n = len(b)
    maxlen = max(m,n)
    result = ''
    carry = 0

    for i in range(maxlen):

        '''
            start from last digit , if digit not found use 0
        '''
        x = int(a[m-1-i]) if i < m else 0
        y = int(b[n-1-i]) if i < n else 0

        '''
            simple add , carry
        '''
        sum = x + y + carry
        result = str(sum%2) + result
        ''' result till now is 1 , now add 0 to the LEFT --> 01  '''
        carry = sum//2 # single / for python 2

    if carry > 0:
        result = '1' + result

    return result

print(addBinary(a,b))
