a = int(input())
b = int(input())
c = int(input())
numb = str(a*b*c)
emList = [0]*10

for i in numb:
    emList[int(i)]+=1

for i in range(len(emList)):
    print(emList[i])