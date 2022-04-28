def hanSu(n):
    if n<100:
        return True
    else :
        iarr=numbToList(n)
        piv=iarr[0]-iarr[1]
        for i in range(len(iarr)-1):
            if iarr[i]-iarr[i+1]!=piv:
                return False
        return True
            
def numbToList(numb):
    arr=[]
    for i in str(numb):
        arr.append(int(i))
    return arr

N = int(input())
ans=0
for i in range(1,N+1):
    if hanSu(i)==True:
        ans+=1
print(ans)