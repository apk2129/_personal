s = "leetcode"
d = ["leet", "code"]

def word_break(s, words):
     d = [False] * len(s)
     print("initial d ", d)
     for i in range(len(s)):
         for w in words:
             print("i",i)
             print("s[i-len(w)+1:i+1] ",s[i-len(w)+1:i+1] )
             if w == s[i-len(w)+1:i+1] and (d[i-len(w)] or i-len(w) == -1):
                 d[i] = True
                 print(d)
     return d[-1]

print(word_break(s,d))
