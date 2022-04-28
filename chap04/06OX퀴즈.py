N = int(input())

for i in range(N):
    inpStr=input()
    
    ansList=[0]*len(inpStr)
    numb=1
    for j in range(len(inpStr)):
        if inpStr[j]=='O':
            ansList[j]=numb
            numb+=1
        else:
            numb=1
    print(sum(ansList))