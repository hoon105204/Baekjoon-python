# 자기자신+각 자리수 합
def d(n):
    return n+sNumb(n)

# 각 자리수 합 구하는 함수
def sNumb(numb):
    ans=0
    for i in str(numb):
        ans+=int(i)
    return ans

ansList=[0]*10000
for i in range(1,10000):
    if ansList[i]==0:
        ansList[i]=1
        print(i)
        j=d(i)
        while(j<10000):
            ansList[j]=1
            j=d(j)
    else:
        continue
    