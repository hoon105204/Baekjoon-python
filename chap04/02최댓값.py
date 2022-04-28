maxNumb=0;
maxIndx=0;
indx=0;
while(True):
    try:
        a=int(input())
        indx+=1
        if maxNumb<a:
            maxIndx = indx
            maxNumb=a
    except:
        break
print(maxNumb)
print(maxIndx)