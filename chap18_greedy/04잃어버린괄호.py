# https://www.acmicpc.net/problem/1541
val = input()

tmp = "("
first_zero = True
for i in val:
    if first_zero and i == "0":
        continue
    if i != "+" and i != "-":
        tmp += i
        first_zero = False
    elif i == "+":
        tmp += i
        first_zero = True
    else:
        tmp += ")-("
        first_zero = True
else:
    tmp += ")"

print(eval(tmp))


