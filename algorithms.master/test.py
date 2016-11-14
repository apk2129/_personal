'''
pattern = "abba", str = "dog cat cat dog"  should return true.
pattern = "abba", str = "dog cat cat fish" should return false.
pattern = "aaaa", str = "dog cat cat dog"  should return false.
pattern = "abba", str = "dog dog dog dog"  should return false.

'''

def wordPattern( pattern, str):
    """
    :type pattern: str
    :type str: str
    :rtype: bool
    """
    import collections

    mp1 = {}
    mp2 = {}
    mp3 = collections.defaultdict(list)
    mp4 = collections.defaultdict(list)

    for i in pattern:
        mp1[i] = mp1.get(i , 0) + 1

    for i in str.split():
        mp2[i] = mp2.get(i , 0) + 1

    for i,val in enumerate(pattern):
        mp3[val].append(i)

    for i,val in enumerate(str.split()):
        mp4[val].append(i)

    print(mp1.values())
    print(mp2.values())
    print(mp3)
    print(mp4)

    return sorted(mp1.values()) == sorted(mp2.values()) and \
           sorted(mp3.values()) == sorted(mp4.values())


print(wordPattern(pattern= "abba",str = "dog cat cat dog"))
