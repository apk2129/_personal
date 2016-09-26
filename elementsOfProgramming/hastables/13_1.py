
def oneLinePalindrome_word(s):
    return s==s[::-1]  # O(n)

def log_n_palindrome(s):
    for i in range(len(s)//2):
        if s[i] != s[len(s)-1-i]:
            return False
        return True

def sentence_palindrome(s):
    s2= ''
    for e in s:
        if not e.isalpha():
            continue
        else:
            s2+=e.lower()

    s2==s2[::-1]

def sentence_isPalindrome( s ):
    if len(s)<2: return True

    head = 0
    tail = len(s)-1

    while head<tail:
        print("head",head, s[head])
        print("tail",tail, s[tail])
        print("-----")
        if not s[head].isalnum():
            head += 1
        elif not s[tail].isalnum():
            tail -= 1
        elif s[head].lower() == s[tail].lower():
            print("==")
            head += 1
            tail -= 1
        else:
            return False

    return True


if __name__=="__main__":

    st = "A man, a plan, a canal: Panama"
    s  = "rotator"

    assert(oneLinePalindrome_word(s)==False)
