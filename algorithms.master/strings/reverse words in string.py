s = "the sky is blue"
# "blue is sky the.

def reverse_words_in_a_string(s):

    ''' Three step to reverse'''
    ''' 1--> reverse the whole sentence'''
    s = s[::-1]

    ''' 2--> reverse each word'''
    start = 0
    end   = 0
    result = ''
    for i in range(len(s)):
        if s[i] == ' ':
            result += reverse(s[start:i]) + " "
            start = i + 1


    '''3--->reverse the last word, if there is only one word this will solve the corner case'''
    result += reverse(s[start:len(s)])
    return result


def reverse( word):

    print(word)
    return word[::-1]
    # def reverse(test):
    # n = len(test)
    # x=""
    # for i in range(n-1,-1,-1):
    #     x += test[i]
    # return x
    '''cant swap letter in a word STRING IS IMMUTABLE in python'''

print(reverse_words_in_a_string(s))




def reverseWords(self, s):
    self.reverse(s, 0, len(s) - 1)

    beg = 0
    for i in xrange(len(s)):
        if s[i] == ' ':
            self.reverse(s, beg, i-1)
            beg = i + 1
        elif i == len(s) -1:
            self.reverse(s, beg, i)

def reverse(self, s, start, end):
    while start < end:
        s[start], s[end] = s[end], s[start]
        start += 1
        end -= 1
