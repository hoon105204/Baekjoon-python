a = int(input())
x = 0
b = a
while True:
    x+=1
    i = b//10
    j = b%10
    b = j*10 + (i+j)%10
    if b == a:
        break
print(x)