def palindromePairs( words):
    d, res = dict([(w[::-1], i) for i, w in enumerate(words)]), []

    print(d) # {'bat': 1, 'tab': 0, 'tac': 2}  ulta karun store kelay


    for i, w in enumerate(words):
        for j in range(len(w)+1):
            prefix, postfix = w[:j], w[j:]
            print("prefix",prefix)
            print("postfix",postfix)

            if prefix in d and i != d[prefix] and postfix == postfix[::-1]:
                res.append([i, d[prefix]])
            if j>0 and postfix in d and i != d[postfix] and prefix == prefix[::-1]:
                res.append([d[postfix], i])
        print("-------")
    return res


s = ["bat", "tab", "cat"]
print(palindromePairs(s))
