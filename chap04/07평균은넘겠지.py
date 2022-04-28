N = int(input())

for k in range(N):
    num=0
    sList=list(map(int,input().split()))
    avg=sum(sList[1:])/(len(sList)-1)
    # 평균을 넘는 사람수 구하기
    for i in range(1,len(sList)):
        if sList[i]>avg:
            num+=1
    ans=num/(len(sList)-1)
    print("{:.3f}%".format(ans*100))
    