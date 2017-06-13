s = ["this","not" ,"an","example","of"]

def get_current_word( p ):

    end = p
    start=p

    while t[end] != " ":
        end = end + 1
    while t[start] != " ":
        start = start - 1

    print("current word : " , t[start+1:end+1] )
    return t[start+1:end+1] 

def is_this_valid_word(word):
    return False

t = ' '.join(s)
bucket = 7

sp = 0
ep = 0

result = []
while ep < len(t):
    line = ""
    ep = ep + bucket
    print("string in to considerations : " + t[sp:ep+1])
    if is_this_valid_word(get_current_word(ep)):
        line = line +  t[sp:ep+1]
    else:
        temp_p = ep
        print(temp_p)
        while t[temp_p]!=" ":
            temp_p = temp_p - 1
        no_of_spaces = ep - temp_p

        #start pointer at the begining of next word
        sp = temp_p

        line += t[sp:temp_p]  #first word
        #append space till bucketsize
        spaces = bucket - (temp_p - sp)
        line += ''.join([" "]*spaces)

    result.append(line)
    print("result",result)
