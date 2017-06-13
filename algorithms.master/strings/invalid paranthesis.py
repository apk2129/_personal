s = "()))"
s = list(s)

for i in s :
    if i == '(':
        # p = s.find(")")
        s.remove("(")
        s.remove(")")


print(s)
