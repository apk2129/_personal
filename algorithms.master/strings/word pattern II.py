'''
pattern = "abab", str = "redblueredblue" should return true.
pattern = "aaaa", str = "asdasdasdasd" should return true.
pattern = "aabb", str = "xyzabcxzyabc" should return false.

'''

def wordPatternMatch( pattern, str):
    pattern_to_word_map = {}
    st                  = set()

    return isMatch(str, 0, pattern, 0, pattern_to_word_map, st)

def isMatch( str, i, pat, j,pattern_to_word_map, st):

    '''base case'''
    if i == len(str) and j == len(pat): return True
    if i == len(str) or  j == len(pat): return False

    '''get current pattern character'''
    c = pat[j]
    print("c ",c)
    '''if the pattern character exists'''
    if c in pattern_to_word_map:

        s = pattern_to_word_map[c]
        print("S ",s)
        '''then check if we can use it to match str[i...i+s.length()]'''
        print(i,i+len(s)-1 )
        print("str[i:i+len(s)-1]  ",str[i:i+len(s)-1] )
        if s != str[i:i+len(s)-1] : return False

        '''if it can match, great, continue to match the rest'''
        return isMatch(str, i + len(s), pat, j + 1, pattern_to_word_map, st)


    '''pattern character does not exist in the map'''
    for k in range(i,len(str)):

        p = str[i:k + 1]
        if p in st: continue

        '''create or update it'''
        pattern_to_word_map[c] = p
        st.add(p)

        '''continue to match the rest'''
        if (isMatch(str, k + 1, pat, j + 1, pattern_to_word_map, st)): return True

        '''backtracking'''
        pattern_to_word_map.pop(c)
        st.remove(p)

    '''we've tried our best but still no luck'''
    return False



print(wordPatternMatch(pattern= "abba",str = "redblueredblue"))
