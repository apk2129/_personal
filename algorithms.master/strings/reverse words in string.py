s = "the sky is blue"
# return "blue is sky the".
stack = ' '.join(s.split()[::-1])

print(stack)
