'''
pattern = "abba", str = "dog cat cat dog"  should return true.
pattern = "abba", str = "dog cat cat fish" should return false.
pattern = "aaaa", str = "dog cat cat dog"  should return false.
pattern = "abba", str = "dog dog dog dog"  should return false.

'''

''' leet code solution '''
def wordPattern( pattern, str):

    arr              = str.split()
    pattern_to_word  = {}

    if(len(arr) != len(pattern)): return False

    for i in range(len(arr)):

        if pattern[i] in pattern_to_word:
            if pattern_to_word[pattern[i]] != arr[i]:
                return False
        elif arr[i] in pattern_to_word.values():
            return False
        else:
            pattern_to_word[pattern[i]] = arr[i]

    print(pattern_to_word)
    return True


print(wordPattern(pattern= "abba",str = "dog cat cat dog"))
