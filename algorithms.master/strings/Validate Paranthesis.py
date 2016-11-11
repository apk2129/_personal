s = "(){}{}{}{}[]]"

stack = []
for b in s:
    print( "b",b)
    if b== '}':
        if not stack or stack.pop() != '{':
            print(False)
    if b== ')':
        if stack and stack.pop() == '(':
            continue
        else:
            print(False)
    if b== ']':
        if not stack or stack.pop() != '[':
            print(False)
    else:
        stack.append(b)
        print(stack)

print("---",stack)

if not stack:print(True)
else: print(False)
