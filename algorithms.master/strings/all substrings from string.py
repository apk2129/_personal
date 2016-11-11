s = 'abababababababababababababababababab'

# Will contain all the possible substrings
substrings = set()

# Get all the possible substrings from the main string
for count in range(0, len(s)):
   for subStrLen in range(0, len(s) - count):
       substrings.add(s[count:count + subStrLen + 1])

print(substrings)
