n1 = '90'
n2 = '9'

add_arr = []

for  position, digit  in enumerate(n2):

    temp = ''
    suffix_zero = len(n2) - position - 1
    print(suffix_zero)

    for i in range(suffix_zero):
        temp += '0'


    print(temp)
    carry   = 0
    mul_res = ''

    for d in n1[::-1]:
        mul     = (int(d) * int(digit)) + carry
        print(mul)
        carry   = mul//10
        print(carry)
        mul_res = str(mul%10) + mul_res
        print(mul_res)

    temp = str(carry) + mul_res + temp
    add_arr.append(temp)

final = 0
for i in add_arr:
    final += int(i)
print("------",final)
